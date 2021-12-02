#!/usr/bin/env python3

"""Script to store the `.po` file in each pre_check.py scripts
"""

from pathlib import Path
import tarfile
import lzma
import base64
import io

po = Path("check.po").read_bytes()
po = lzma.compress(po, preset=lzma.PRESET_EXTREME)
po = base64.b64encode(po)

for file in Path(".").glob("*/*/wording_en.md"):
    exercise = file.parent
    pre_check = exercise / "pre_check.py"
    if (exercise / "testenv").exists():
        tar = io.BytesIO()
        with tarfile.open(fileobj=tar, mode="w:xz") as t:
            t.add(exercise / "testenv", arcname=".")
        decompressor = f"""
tar_bytes = io.BytesIO(base64.b64decode({base64.b64encode(tar.getvalue())!r}))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")
        """
    else:
        decompressor = ""
    pre_check.write_text(
        f"""# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

po = base64.b64decode({po!r})
po = lzma.decompress(po)
LC_MESSAGES = Path(".") / "fr" / "LC_MESSAGES"
LC_MESSAGES.mkdir(parents=True, exist_ok=True)
(LC_MESSAGES / "check.po").write_bytes(po)
run(["msgfmt", str(LC_MESSAGES / "check.po"), "--output-file",
     str(LC_MESSAGES / "check.mo")])

{decompressor}

if Path("solution").exists():
    Path("solution").rename("solution.py")
""",
        encoding="UTF-8",
    )
