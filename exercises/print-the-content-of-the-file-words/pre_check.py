# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AIxdABcLvBx9AZXAMzmZXGs1sHxm1kMiRwkeeBumwiMg004DOoE/QcYZlp2py5lQ5+6m5G5NZI3KYEpR2MUrT8kxMm+77uaYVteTcqnWMm/Uq3SewocP3ygMrdIf8q4qm7PjK6LKIuE8ipolJMVQLhtWxyMw5vcUFQQZh4Uh8viIs/G0Sscefkb2rtVJEjT8ACTC0wnkAV9jAAGoAYBQAABl9p+KscRn+wIAAAAABFla'))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
