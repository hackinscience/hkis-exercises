# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AQ1dABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9ZtDr1mWPVPH6aIl9xQ3gEeugE1XdGichyw8TLgSZ18cONWBR64gUckn0Lc7jkrbQ3kkJbySrsbmLkDtsl6ABR1kzdf+I0SCOMBgGFCgt35uUIWGz2dlhHv3zJFSdtwNo402npkiOOfaunMJABlWW6dPt8nQi1KL3t86p9CQwFlOFmYdRvr4h5li82H6RpQsWxZ/O0EkH5EQHAa6gSE+lCrfMAyvPYde+wD8nKgJN+vLeBcDhBpQJUEaeRYMrUeuMdQ68MraDVIC1LkqAAAAAANfovTWGG2a2AAGpAoBQAAAQX2MGscRn+wIAAAAABFla'))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
