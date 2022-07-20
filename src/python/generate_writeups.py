import os
import json
import shutil

from typing import Dict, Optional, Tuple


TEMPLATE_FILE_NAME = "writeup.tmpl.md"
SPEC_FILE_NAME = "spec.json"
OUTPUT_FILE_NAME_FORMAT = "{title}.md"


def format_if_present(fmt: str, entry: Optional[str]) -> str:
    if entry is None:
        return ""
    return fmt.format(entry)


def read_if_file(cwd: str, entry: str) -> str:
    if not "\n" in entry and entry.endswith(".fragment.md"):
        with open(os.path.join(cwd, entry), "r") as f:
            return f.read()
    return entry


def render_spec(template: str, cwd: str, spec: Dict[str, str]) -> Tuple[str, str]:
    format_args = {
        "title": spec["title"],
        "author": format_if_present("> {}\n", spec.get("author")),
        "points": spec["points"],
        "question": read_if_file(cwd, spec["question"]),
        "solution": read_if_file(cwd, spec["solution"]),
        "flag": spec["flag"],
    }
    return OUTPUT_FILE_NAME_FORMAT.format(**format_args), template.format(**format_args)


def main() -> None:
    current_dir = os.path.dirname(__file__)
    top_level_dir = os.path.join(current_dir, "..", "..")
    data_dir = os.path.join(top_level_dir, "src", "data")
    output_dir = os.path.join(top_level_dir, "writeups")

    with open(os.path.join(data_dir, TEMPLATE_FILE_NAME)) as f:
        template = f.read()

    shutil.rmtree(output_dir, ignore_errors=True)

    for root, source_dirs, _ in os.walk(data_dir):
        for source_dir in source_dirs:
            source_dir = os.path.join(root, source_dir)
            source_spec = os.path.join(source_dir, SPEC_FILE_NAME)

            if not os.path.exists(source_spec):
                # Not a bottom-level writeup directory.
                continue

            with open(source_spec, "r") as f:
                output_file, output_file_contents = render_spec(
                    template, source_dir, json.loads(f.read())
                )

            output_file_dir = os.path.join(output_dir, os.path.relpath(root, data_dir))
            os.makedirs(output_file_dir, exist_ok=True)

            output_file = os.path.join(output_file_dir, output_file)
            with open(output_file, "w") as f:
                f.write(output_file_contents)

            print(f"Rendered `{os.path.relpath(output_file, top_level_dir)}`")


if __name__ == "__main__":
    main()
