from __future__ import annotations

from pathlib import Path

from kirsten_work_os_kernel.branch_builder import build_branch_packet, branch_packet_to_markdown
from kirsten_work_os_kernel.brief_builder import build_brief
from kirsten_work_os_kernel.signal_intake import intake_signal

ROOT = Path(__file__).resolve().parents[1]
OPPORTUNITY = ROOT / "examples" / "phd-outreach" / "google_phd_outreach_opportunity.json"
PROFILE = ROOT / "data" / "canonical" / "profile" / "kirsten_profile.json"
SIGNAL = ROOT / "examples" / "phd-outreach" / "google_phd_outreach_signal.json"


def test_build_branch_packet_links_opportunity_and_profile():
    packet = build_branch_packet(OPPORTUNITY, PROFILE)
    assert packet["branch_id"] == "phd-outreach"
    assert packet["organization"] == "Google"
    assert "evidence.resume.director_residence_life" in packet["evidence_refs"]
    assert "phd-outreach-intelligence-dashboard" in packet["portfolio_projects"]


def test_branch_packet_markdown_is_human_readable():
    packet = build_branch_packet(OPPORTUNITY, PROFILE)
    md = branch_packet_to_markdown(packet)
    assert "Branch Packet" in md
    assert "Candidate positioning" in md
    assert "Recommended next actions" in md


def test_build_brief_contains_core_message():
    brief = build_brief(OPPORTUNITY, PROFILE)
    assert "university ecosystem strategist" in brief
    assert "data-informed outreach" in brief
    assert "Risk to manage" in brief


def test_intake_signal_record_is_review_bounded():
    record = intake_signal(SIGNAL)
    assert record["status"] == "captured_for_review"
    assert record["branch_id"] == "phd-outreach"
    assert "Promote only reviewed facts" in " ".join(record["next_steps"])
