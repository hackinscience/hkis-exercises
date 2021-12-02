# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AMddABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9aDo+XtwI2qf5PLhgG85YJynwzcOvxlWvi7F39N6KNj12xh+MQjUEfto6SCXCVDvHJIvNHYOYpI/KF7OYHIXX9av3V62Pvs4X/kQv2f+bELK1N+pKpCb7o7mnYhJlB+ZJgokJb+KKpjKmBNkwCjtYochtIeRK1taO9QYhSqVuJfDb/oeDHAAAAEpMFofOp3OqAAHjAYBQAADKDADvscRn+wIAAAAABFla'))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
