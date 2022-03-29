# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/ANVdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9aDo+XtwI2qf5PLhgG85YJynwzcOvxlWvi7FkP/fKm2rUK1iXmMJWHPkWiDQwmwxwvMZ5BP0sP/uIKXcdg/xx1LaVsmIrGpk8gwLTYhaNx1Aw9Ce5IoeVmn80oaaUI7mQuUJSQOR4wvgdcHXG84GZBDwkkRoryJhKxW6KkgdBRnOZ6E1xI2cT49Y9qOy6CYdftTIa5QAAAAD0P/uvmy+rZQAB8QGAUAAAWq8eobHEZ/sCAAAAAARZWg=='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
