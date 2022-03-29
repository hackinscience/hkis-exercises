# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/ANtdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9Z8KqXJoAerAd9lwEAuSOQyyLHKJcx2mLmDZmZnVN6zs/aVGO0wJZpUhk3VSZWzzccKcG3sM7JTJQ5A2Qgiqs5/X0VWSa94b4JpzMwQJnFGyMnfyVPzztrRXzDFsoIRKOq2fgzsVQyAGjRi3FdKsyRz+517PjmHBTROQaSdQipYx+jtrF/+qa7nl5R+Qp660Qpd0TtWfCXnV6QAAAquAp5KIsOf4AAfcBgFAAAEdMR3exxGf7AgAAAAAEWVo='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
