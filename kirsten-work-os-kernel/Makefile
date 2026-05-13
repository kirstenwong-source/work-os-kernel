.PHONY: test validate brief branch signal

test:
	python -m pytest

validate:
	python -m kirsten_work_os_kernel validate --root .

branch:
	python -m kirsten_work_os_kernel build-branch --opportunity examples/phd-outreach/google_phd_outreach_opportunity.json --profile data/canonical/profile/kirsten_profile.json --out data/runtime/phd_outreach_branch_packet.json

brief:
	python -m kirsten_work_os_kernel build-brief --opportunity examples/phd-outreach/google_phd_outreach_opportunity.json --profile data/canonical/profile/kirsten_profile.json --out data/runtime/phd_outreach_brief.md

signal:
	python -m kirsten_work_os_kernel intake-signal --signal examples/phd-outreach/google_phd_outreach_signal.json --out data/runtime/phd_outreach_signal_record.json
