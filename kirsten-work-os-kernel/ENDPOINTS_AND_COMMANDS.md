# Endpoints And Commands

This repository has no HTTP server, background daemon, external connector, live web crawler, scheduled job, model-calling service, or production endpoint.

All commands are local CLI commands.

## Validate

```bash
python -m kirsten_work_os_kernel validate --root .
```

Purpose: checks repo structure, registries, schemas, branches, and governed example objects.

## Build branch

```bash
python -m kirsten_work_os_kernel build-branch \
  --opportunity examples/phd-outreach/google_phd_outreach_opportunity.json \
  --profile data/canonical/profile/kirsten_profile.json \
  --out data/runtime/phd_outreach_branch_packet.json
```

Purpose: creates a local branch packet that connects an opportunity to Kirsten's canonical profile, evidence, and branch strategy.

## Build brief

```bash
python -m kirsten_work_os_kernel build-brief \
  --opportunity examples/phd-outreach/google_phd_outreach_opportunity.json \
  --profile data/canonical/profile/kirsten_profile.json \
  --out data/runtime/phd_outreach_brief.md
```

Purpose: creates a plain-English strategy brief suitable for reviewing the opportunity and explaining the candidate positioning.

## Intake signal

```bash
python -m kirsten_work_os_kernel intake-signal \
  --signal examples/phd-outreach/google_phd_outreach_signal.json \
  --out data/runtime/phd_outreach_signal_record.json
```

Purpose: converts a local signal into a structured runtime record.

## Test suite

```bash
python -m pytest
```

Purpose: runs unit tests used by GitHub Actions.
