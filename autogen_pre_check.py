#!/usr/bin/env python3

"""Script to compress `testenv` directories into pre_check.py files.

This is usefull for exercises needing some static files.
"""

from pathlib import Path
import tarfile
import base64
import io


def reset(tarinfo):
    tarinfo.uid = tarinfo.gid = 0
    tarinfo.uname = tarinfo.gname = "root"
    tarinfo.mtime
    return tarinfo


def main():
    for file in Path(".").glob("*/*/wording_en.md"):
        exercise = file.parent
        pre_check = exercise / "pre_check.py"
        if (exercise / "testenv").exists():
            tar = io.BytesIO()
            with tarfile.open(fileobj=tar, mode="w:xz") as t:
                t.add(exercise / "testenv", arcname=".", filter=reset)
            extractor = f"""# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode({base64.b64encode(tar.getvalue())!r}))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
"""
            pre_check.write_text(
                extractor,
                encoding="UTF-8",
            )


if __name__ == "__main__":
    main()
