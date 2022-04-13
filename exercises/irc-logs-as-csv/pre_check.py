# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AMRdABcLvBx9AZXAMzmZXGs1sHxm1kMiRwkeeBumwiMg004DOoE/QcYZlp2py5lQ5+6m1lpIOjIIoodJX/BAc7gx8mypHVdn+PVpZFtZDOQCNjZn0Og7cH37wPy0EH09Jauee53T1qdpadW3oJJG70OEad8ny4dsEWWRSr9ifG+HT6yH0gAEOuC4anCbroUici3fT+TvlQeOhx6IzehWDnOGCm5/tP6mu/3rCLqRxk/Yj3aVM0Ddisc5oL2j66HyQBeFuBUF6wAAxkfKI+Ayw7IAAeABgFAAAGR+lGmxxGf7AgAAAAAEWVo='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
