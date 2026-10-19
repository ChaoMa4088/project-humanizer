"""Check this skill repository using only the Python standard library."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def validate(root):
    required = ["SKILL.md", "agents/openai.yaml", "references/code.md",
                "references/documents.md", "README.md"]
    for name in required:
        if not (root / name).is_file():
            raise ValueError(f"Missing file: {name}")
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml", ".py"}:
            content = path.read_text(encoding="utf-8")
            if "\ufffd" in content:
                raise ValueError(f"Replacement character: {path}")
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", skill, re.S)
    if not match:
        raise ValueError("Missing frontmatter")
    metadata = dict(line.split(":", 1) for line in match[1].splitlines() if ":" in line)
    if metadata.get("name", "").strip() != "project-humanizer":
        raise ValueError("Unexpected skill name")
    if not metadata.get("description", "").strip():
        raise ValueError("Empty description")
    for path in [root / "SKILL.md", *sorted((root / "references").glob("*.md"))]:
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
                raise ValueError(f"Invalid reference: {target}")
    interface = (root / "agents/openai.yaml").read_text(encoding="utf-8")
    if not interface.startswith("interface:\n"):
        raise ValueError("Missing interface metadata")
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(r'^  ' + key + r': "[^"\n]+"$', interface, re.M):
            raise ValueError(f"Invalid interface field: {key}")
    if "$project-humanizer" not in interface:
        raise ValueError("Default prompt must invoke the skill")


if __name__ == "__main__":
    validate(ROOT)
    print("Skill repository checks passed.")
