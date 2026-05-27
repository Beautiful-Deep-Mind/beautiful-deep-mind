# bdm-core

Core package for the Beautiful Deep Mind project.

Contains the foundational cognitive architecture layers:

- `bdm.memory` — event schema, short-term buffer, long-term store, episodic records
- `bdm.reflection` — consistency review loop
- `bdm.self_model` — internal state representation
- `bdm.continuity` — cross-session context persistence

## Status

Early prototype. APIs are unstable and will change.

## Install (development)

```bash
pip install -e ".[dev]"
```

## Run tests

```bash
pytest
```
