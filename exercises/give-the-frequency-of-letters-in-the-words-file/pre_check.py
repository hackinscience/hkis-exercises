# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AOBdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9Zs4YHJSSfp2j8wtY9VmVpN861omP7GmOfsB3eptwTrTOhltxI1Xp5YNU9gZlXvARgBG3o0sk47utrNdEr7G/7AhVUgLsmnl4S6ahmNfXRI/06eJSj2V/maWYUD+N5reJ/iNpc4AByyFZZ+qp9JlIJN2np7Ezx56pEANlLVT4/eYaPxgpSWovxnCdBexxKYxyT8SZO+JH4FI7ujQc4C9gANrS6iInaCgiAAH8AYBQAACEvIAdscRn+wIAAAAABFla'))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
