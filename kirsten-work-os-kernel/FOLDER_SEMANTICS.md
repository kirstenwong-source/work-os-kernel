# Folder Semantics

## `governance/`

Rules for how the kernel changes. This is policy, not raw evidence.

## `registry/`

Machine-readable discovery surfaces. Registries should point to real files.

## `schemas/`

Contracts for objects such as profile, opportunity, branch, evidence, artifact request, and signal.

## `data/canonical/`

Stable, reviewed career evidence and reusable profile facts.

## `data/evidence/`

Evidence objects that support claims, stories, and fit maps.

## `data/runtime/`

Generated files and temporary outputs. Runtime files can be regenerated and should not be treated as source truth.

## `branches/`

Workstreams that branch from the kernel. Each branch should have a `branch.json` contract and human-readable strategy files.

## `examples/`

Safe examples and synthetic inputs used by tests and documentation.

## `src/`

Local Python command implementation.

## `tests/`

Validation and regression tests.
