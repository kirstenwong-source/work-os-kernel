# How To Branch A New Workstream

Use this process whenever a new job, portfolio project, research direction, or networking strategy needs its own lane.

## Step 1: Create branch folder

Copy:

```text
branches/_template/
```

Rename it with a stable slug:

```text
branches/<new-branch-slug>/
```

Examples:

- `branches/dean-of-students/`
- `branches/phd-outreach/`
- `branches/dissertation-translation/`

## Step 2: Create or update branch contract

Edit `branch.json` with:

- branch id
- title
- purpose
- active opportunity ids
- evidence ids
- artifact targets

## Step 3: Add opportunity or signal object

Place examples in:

```text
examples/<branch-slug>/
```

Use `schemas/opportunity.schema.json` or `schemas/work-signal.schema.json`.

## Step 4: Register the branch

Add the branch to:

```text
registry/branch-registry.json
```

## Step 5: Validate

Run:

```bash
python -m kirsten_work_os_kernel validate --root .
python -m pytest
```
