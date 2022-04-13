# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/ANxdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9Zs4YHJSSfp2j8wtY9VmVpN861o5HIHOr9eq+Zn1QmkzdNU6uNXBeObTRIG+Ejid+i5oVtM72mTI9qLKc2DFvZR6vbTramaDYZ3K0q7dcoi0AKW3JDqB1AGqnN4hRDRv0gRhQcDI9AyCPLzNN2Np+B11BrSWJJk40xzKDeq18suBgMvDYyLlsQ//fjKd2TJdDEYXQs9SnebzGwr4ANSCY7D+GAZ8AAfgBgFAAAJL+EYaxxGf7AgAAAAAEWVo='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
