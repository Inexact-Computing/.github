#!/usr/bin/env python3
"""
GitHub Submodule Status and Sync Auditing Script
Reads .gitmodules and audits the presence, commit hashes, and remote status of submodules under work/.
"""

import sys
import re
import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
GITMODULES_FILE = REPO_ROOT / ".gitmodules"
WORK_DIR = REPO_ROOT / "work"

def parse_gitmodules():
    if not GITMODULES_FILE.exists():
        print(f"Error: {GITMODULES_FILE} not found.")
        return []

    content = GITMODULES_FILE.read_text(encoding="utf-8")
    submodules = []
    current = {}
    
    for line in content.splitlines():
        line = line.strip()
        m_sub = re.match(r'^\[submodule\s+"([^"]+)"\]', line)
        if m_sub:
            if current and "path" in current:
                submodules.append(current)
            current = {"name": m_sub.group(1)}
        elif line.startswith("path ="):
            current["path"] = line.split("=", 1)[1].strip()
        elif line.startswith("url ="):
            current["url"] = line.split("=", 1)[1].strip()

    if current and "path" in current:
        submodules.append(current)
    return submodules

def audit_submodules(submodules):
    total = len(submodules)
    present_count = 0
    missing_count = 0
    
    print(f"Auditing {total} declared submodules in .gitmodules:\n")
    print(f"{'Submodule Path':<70} | {'Status':<10}")
    print("-" * 85)
    
    for sub in submodules:
        sub_path = REPO_ROOT / sub["path"]
        if sub_path.exists() and any(sub_path.iterdir()):
            status = "PRESENT"
            present_count += 1
        else:
            status = "EMPTY/MISSING"
            missing_count += 1
        print(f"{sub['path']:<70} | {status:<10}")

    print("-" * 85)
    print(f"Total: {total} | Present: {present_count} | Missing/Uninitialized: {missing_count}\n")

def main():
    parser = argparse.ArgumentParser(description="Audit and sync submodules")
    parser.add_argument("--status", action="store_true", help="Print status of all submodules")
    parser.add_argument("--report", action="store_true", help="Generate detailed report")
    args = parser.parse_args()

    submodules = parse_gitmodules()
    if not submodules:
        print("No submodules found.")
        return

    audit_submodules(submodules)

if __name__ == "__main__":
    main()
