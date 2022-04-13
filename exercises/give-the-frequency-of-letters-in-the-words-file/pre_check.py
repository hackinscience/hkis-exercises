# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AI5dABcLvBx9AZXAMzmZXGs1sHxm1kMiRwkeeBumwiMg004DOoE/QcYZlp2py5lQ5+6m5G5NZI3KYEpR2MUrT8kxMm+77yFnuXad0VotxkQBnZSA56y6KPhAchaXb0ujLxfJZT9c/lCHr4lOxZ5lO18beXS85F3zvap1Bdal1AA1PcM8I1pWLF25hBiEb6P3HQAAAAAJjZc2+smb7QABqgGAUAAAbldXx7HEZ/sCAAAAAARZWg=='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
