# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/ANBdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9Zs4YHJSSfp2j8wtY9VmVpN861omP7GmOfsCCn+37GEsgSjLBrFmQ+UGmcjMYLz+pcU5/4NQeBj0WpAtLYgaNc6lbvDS9cACwOmpFBqRyoz3c62Dhh+1fmFz2UQr08QxcVqeE62tcw1OqIZekrVAvDRSxZWngNv298W2SXRaRZC0rSdDkHd5zbxDzsv6PmwAAaPo6nL2KBcQAAewBgFAAAB++Vh6xxGf7AgAAAAAEWVo='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
