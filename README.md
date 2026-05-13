Kirsten Work OS Kernel
A reusable operating-system kernel for career strategy, research translation, portfolio projects, outreach, applications, interview preparation, and professional storytelling.

This repository is adapted from a three-plane operating model:

Control plane - canonical meaning, schemas, source-of-truth registries, policies, and evidence rules.
Evidence plane - source logs, evidence packets, decision records, and append-only runtime outputs.
Execution plane - local commands that read the control plane, generate work products, and validate that outputs stay grounded.
The kernel is designed so every major workstream can branch from one governed foundation. The first included branch is phd-outreach, built to support the Google PhD Outreach Program Manager opportunity and related academic-partnership portfolio work.

What this repo is for
Use this kernel to organize and reuse work across:

PhD outreach and university partnership roles
Dean, director, and student affairs leadership roles
Dissertation-to-career translation
Job-fit maps and cover letters
Interview story banks
Portfolio projects and GitHub demonstrations
Networking and stakeholder strategy
Professional identity, thought leadership, and long-term career positioning
What this repo is not
This is not a production recruiting system, applicant-tracking system, web crawler, or automated application tool. It does not use private student records, private employer records, or live external APIs. It is a local-first knowledge and work-product kernel.

Repository layout
.
├── README.md
├── AI_WORK_START_HERE.md
├── AI_TABLE_OF_CONTENTS.md
├── DATA_FLOW_MAP.md
├── ENDPOINTS_AND_COMMANDS.md
├── AGENTS.md
├── FOLDER_SEMANTICS.md
├── RECENT_WORK.md
├── .github/workflows/ci.yml
├── branches/
│   ├── _template/
│   └── phd-outreach/
├── data/
│   ├── canonical/
│   ├── evidence/
│   └── runtime/
├── docs/
├── examples/
├── governance/
├── registry/
├── schemas/
├── scripts/
├── src/kirsten_work_os_kernel/
└── tests/
Quick start
Install locally:

python -m pip install -e .[dev]
Validate the repo:

python -m kirsten_work_os_kernel validate --root .
Generate a branch packet for the included PhD outreach example:

python -m kirsten_work_os_kernel build-branch \
  --opportunity examples/phd-outreach/google_phd_outreach_opportunity.json \
  --profile data/canonical/profile/kirsten_profile.json \
  --out data/runtime/phd_outreach_branch_packet.json
Generate a hiring-manager-facing brief:

python -m kirsten_work_os_kernel build-brief \
  --opportunity examples/phd-outreach/google_phd_outreach_opportunity.json \
  --profile data/canonical/profile/kirsten_profile.json \
  --out data/runtime/phd_outreach_brief.md
Run tests:

python -m pytest
Core operating rule
Canonical evidence should be changed deliberately. Runtime outputs should not rewrite source truth directly.

A safe flow is:

source or signal
-> evidence object
-> opportunity object
-> branch packet
-> artifact request
-> human review
-> promotion decision
-> canonical update, if approved
Included branch: PhD outreach
The branches/phd-outreach/ folder includes:

a branch contract
a role-fit map
a 90-day operating plan
an outreach dashboard specification
an example Google PhD outreach opportunity object
an example signal object
This branch demonstrates how the kernel can support a specific opportunity without contaminating the canonical career evidence layer.

Sample outputs
The repo includes generated sample outputs under examples/phd-outreach/outputs/ so reviewers can see what the commands produce without running the CLI first. Runtime outputs generated during local work should go under data/runtime/ and remain draft-only until reviewed.

GitHub green checks
The included GitHub Actions workflow runs:

Python package installation
Unit tests
Repository validation
Branch packet generation
Brief generation
Signal intake
If the files are uploaded as-is to a GitHub repository, the ci workflow should pass.
