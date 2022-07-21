import os
import json
import shutil
from argparse import ArgumentParser
from dataclasses import dataclass
from urllib.parse import quote as url_escape

from typing import Dict, List, Optional


TEMPLATE_FILE_NAME = "writeup.tmpl.md"
SPEC_FILE_NAME = "spec.json"
OUTPUT_FILE_NAME_FORMAT = "{title}.md"


@dataclass
class SpecOutput:
    writeup_name: str
    file_name: str
    file_contents: str
    attachments: List[str]


class SpecRenderer:
    def __read_spec_template(self, data_dir: str):
        with open(os.path.join(data_dir, TEMPLATE_FILE_NAME)) as f:
            return f.read()

    def __call_if_present(self, fn: callable, entry: Optional[str], *args) -> str:
        if entry is None:
            return ""
        return fn(*args, entry)

    def __read_if_file(self, cwd: str, entry: str) -> str:
        if not "\n" in entry and entry.endswith(".fragment.md"):
            with open(os.path.join(cwd, entry), "r") as f:
                return f.read()
        return entry

    def __init__(self, data_dir):
        self.template = self.__read_spec_template(data_dir)

    def render(self, cwd: str, ctf_path: str, spec: Dict[str, str]) -> SpecOutput:
        format_args = {
            "title": os.path.join(ctf_path, spec["name"]),
            "author": self.__call_if_present(str.format, spec.get("author"), "> {}\n"),
            "points": spec["points"],
            "question": self.__read_if_file(cwd, spec["question"]).strip(),
            "attachments": self.__call_if_present(
                lambda attachments: "\n\n"
                + ", ".join(
                    map(
                        lambda attachment: f"[{attachment}]({os.path.join('attachments', url_escape(spec['name']), attachment)})",
                        attachments,
                    )
                ),
                spec.get("attachments"),
            ).strip(),
            "solution": self.__read_if_file(cwd, spec["solution"]).strip(),
            "flag": spec["flag"],
        }
        return SpecOutput(
            writeup_name=spec["name"],
            file_name=OUTPUT_FILE_NAME_FORMAT.format(title=spec["name"]),
            file_contents=self.template.format(**format_args),
            attachments=spec.get("attachments", []),
        )


def main(check: bool) -> None:
    current_dir = os.path.dirname(__file__)
    top_level_dir = os.path.join(current_dir, "..", "..")
    data_dir = os.path.join(top_level_dir, "src", "data")
    output_dir = os.path.join(top_level_dir, "writeups")

    renderer = SpecRenderer(data_dir)

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
                spec_output = renderer.render(source_dir, ctf_dir, json.loads(f.read()))

            output_file_dir = os.path.join(output_dir, ctf_dir)
            os.makedirs(output_file_dir, exist_ok=True)

            output_file = os.path.join(output_file_dir, spec_output.file_name)
            if check:
                failed = False
                if os.path.exists(output_file):
                    with open(output_file, "r") as f:
                        failed = f.read() != spec_output.file_contents
                else:
                    failed = True
                if failed:
                    print(
                        f"File `{os.path.relpath(output_file, top_level_dir)} needs to be regenerated`"
                    )
                    retval = 1
            else:
                with open(output_file, "w") as f:
                    f.write(spec_output.file_contents)

                for attachment in spec_output.attachments:
                    attachment_dir = os.path.join(
                        output_file_dir, "attachments", spec_output.writeup_name
                    )
                    os.makedirs(attachment_dir, exist_ok=True)
                    shutil.copy(
                        os.path.join(source_dir, attachment),
                        os.path.join(attachment_dir, attachment),
                    )

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
