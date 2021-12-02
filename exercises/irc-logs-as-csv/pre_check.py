# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AQNdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9ZtDr1mWPVPH6aIl9xQ3gEeugE08LAuuHRTVPQjzuZ7EE7TPI9woqRsw6yVUZgGm+HvXO3iUHGuQ+FiDcX0bFNTptMs8j59So1cd+H3bspfw41Ad7iphsonxksX16IwcXAajX2sXPJDWE/lUqhn5HCcvsNFZTh5rb+NIPTNGVLvt69drs/Vj9fbHSLjGQKpxrDbeoCS1UC7B/l+nfPIPdLt7cOqhlH94YkYhZh00kYJOmRa6HWmbqQSBRox6TnLieA7gAAKsATCkl9OePAAGfAoBQAACgu0DUscRn+wIAAAAABFla'))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
