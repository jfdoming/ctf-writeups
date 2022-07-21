import os
import json
import shutil
from argparse import ArgumentParser

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


def render_spec(template: str, cwd: str, ctf_path: str, spec: Dict[str, str]) -> Tuple[str, str]:
    format_args = {
        "title": os.path.join(ctf_path, spec["name"]),
        "author": format_if_present("> {}\n", spec.get("author")),
        "points": spec["points"],
        "question": read_if_file(cwd, spec["question"]).strip(),
        "solution": read_if_file(cwd, spec["solution"]).strip(),
        "flag": spec["flag"],
    }
    return OUTPUT_FILE_NAME_FORMAT.format(title=spec["name"]), template.format(**format_args)


def main(check: bool) -> None:
    current_dir = os.path.dirname(__file__)
    top_level_dir = os.path.join(current_dir, "..", "..")
    data_dir = os.path.join(top_level_dir, "src", "data")
    output_dir = os.path.join(top_level_dir, "writeups")

    with open(os.path.join(data_dir, TEMPLATE_FILE_NAME)) as f:
        template = f.read()

    if not check:
        shutil.rmtree(output_dir, ignore_errors=True)

    retval = 0
    for root, source_dirs, _ in os.walk(data_dir):
        for source_dir in source_dirs:
            source_dir = os.path.join(root, source_dir)
            source_spec = os.path.join(source_dir, SPEC_FILE_NAME)
            ctf_dir = os.path.relpath(root, data_dir)

            if not os.path.exists(source_spec):
                # Not a bottom-level writeup directory.
                continue

            with open(source_spec, "r") as f:
                output_file, output_file_contents = render_spec(
                    template, source_dir, ctf_dir, json.loads(f.read())
                )

            output_file_dir = os.path.join(output_dir, ctf_dir)
            os.makedirs(output_file_dir, exist_ok=True)

            output_file = os.path.join(output_file_dir, output_file)
            if check:
                failed = False
                if os.path.exists(output_file):
                    with open(output_file, "r") as f:
                        failed = (f.read() != output_file_contents)
                else:
                    failed = True
                if failed:
                    print(f"File `{os.path.relpath(output_file, top_level_dir)} needs to be regenerated`")
                    retval = 1
            else:
                with open(output_file, "w") as f:
                    f.write(output_file_contents)

            if not check:
                print(f"Rendered `{os.path.relpath(output_file, top_level_dir)}`")

    if retval:
        print()
        print("Regenerate files with `python3 src/python/generate_writeups.py`")
    return retval


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate writeup documents")
    parser.add_argument("filenames", nargs="*", action="append")
    parser.add_argument("--check", dest="check", action="store_true")
    args = parser.parse_args()
    raise SystemExit(main(args.check))
