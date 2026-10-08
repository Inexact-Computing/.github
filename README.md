# GitHub Organization & Submodule Synchronization (share/github/)

This directory manages synchronization between the monolithic **`inexact-computing-lab`** workspace and individual satellite repositories hosted under the [Inexact-Computing](https://github.com/Inexact-Computing) GitHub organization.

## Registered Submodules

All submodules are declared in [`.gitmodules`](../../.gitmodules).

## Automation Script

Use `sync_submodules.py` to audit submodule health, check synchronization status, and verify git remote targets:

```bash
# Check status of all submodules
python share/github/sync_submodules.py --status

# Generate sync report
python share/github/sync_submodules.py --report
```
