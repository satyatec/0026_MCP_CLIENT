#!/usr/bin/env python3
"""
Claude Code Skills Synchronizer
Generates .claude/skills/ (flat layout required by Claude Code) from the single
source of truth .agents/skills/ (layout used by Antigravity).

  .agents/skills/<name>/                  -> .claude/skills/<name>/
  .agents/skills/downstream/<mcp>/        -> .claude/skills/<mcp>/
"""

import sys
import json
import shutil
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / ".agents" / "skills"
DST = ROOT / ".claude" / "skills"
MANIFEST = DST / ".generated.json"
COPIED_FILES = ("tools.json",)


def generated_banner(src_rel: str) -> str:
    return (f"<!-- GENERADO desde {src_rel} por scripts/sync_claude_skills.py. "
            f"No editar aquí: editar el original y re-sincronizar. -->\n")


def source_skills() -> dict:
    """Maps flat skill name -> source directory."""
    skills = {}
    if not SRC.exists():
        return skills
    for d in sorted(SRC.iterdir()):
        if not d.is_dir():
            continue
        if d.name == "downstream":
            for mcp in sorted(d.iterdir()):
                if mcp.is_dir() and (mcp / "SKILL.md").exists():
                    skills[mcp.name] = mcp
        elif (d / "SKILL.md").exists():
            skills[d.name] = d
    return skills


def render_skill(src_dir: Path) -> str:
    """Returns SKILL.md content with the generated banner inserted after the frontmatter."""
    content = (src_dir / "SKILL.md").read_text(encoding="utf-8")
    banner = generated_banner((src_dir / "SKILL.md").relative_to(ROOT).as_posix())
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            cut = end + len("\n---")
            return content[:cut] + "\n" + banner + content[cut:]
    return banner + content


def expected_files() -> dict:
    """Maps destination path -> expected content (str for text, Path for binary copy)."""
    files = {}
    for name, src_dir in source_skills().items():
        files[DST / name / "SKILL.md"] = render_skill(src_dir)
        for fname in COPIED_FILES:
            if (src_dir / fname).exists():
                files[DST / name / fname] = (src_dir / fname).read_text(encoding="utf-8")
    return files


def previously_generated() -> list:
    if MANIFEST.exists():
        try:
            return json.loads(MANIFEST.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def diff(files: dict) -> list:
    """Returns human-readable list of differences between expected and current state."""
    changes = []
    for path, content in files.items():
        if not path.exists():
            changes.append(f"falta {path.relative_to(ROOT).as_posix()}")
        elif path.read_text(encoding="utf-8") != content:
            changes.append(f"desactualizado {path.relative_to(ROOT).as_posix()}")
    names = {p.parent.name for p in files}
    for old in previously_generated():
        if old not in names and (DST / old).exists():
            changes.append(f"obsoleto .claude/skills/{old}")
    return changes


def sync(files: dict):
    names = sorted({p.parent.name for p in files})
    for old in previously_generated():
        if old not in names and (DST / old).exists():
            shutil.rmtree(DST / old)
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8", newline="\n")
    MANIFEST.write_text(json.dumps(names, indent=2) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera .claude/skills/ a partir de .agents/skills/ (fuente de verdad).")
    parser.add_argument("--check", action="store_true", help="Solo comprobar; exit 1 si .claude/skills/ está desincronizado.")
    parser.add_argument("--quiet", action="store_true", help="No imprimir nada si no hay cambios.")
    args = parser.parse_args()

    files = expected_files()
    changes = diff(files)

    if args.check:
        if changes:
            print(f"{RED}[FAIL] .claude/skills/ desincronizado ({len(changes)}):{RESET}")
            for c in changes:
                print(f"  - {c}")
            print("Ejecuta: python scripts/sync_claude_skills.py")
            sys.exit(1)
        if not args.quiet:
            print(f"{GREEN}[PASS] .claude/skills/ sincronizado con .agents/skills/{RESET}")
        sys.exit(0)

    if changes:
        sync(files)
        print(f"{YELLOW}[SYNC] .claude/skills/ actualizado ({len(changes)} cambios):{RESET}")
        for c in changes:
            print(f"  - {c}")
    elif not args.quiet:
        print(f"{GREEN}[OK] .claude/skills/ ya estaba sincronizado.{RESET}")
