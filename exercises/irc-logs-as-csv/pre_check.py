# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/ARJdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9ZtDr1mWPVPH6aIl9xQ3gEeugE08LAuuHRTU/bvB3ktSq03ooAMK3TB5A+C8yan4PLkpFx7Hy1S8Q3yv7KxobQb8vdCwALZl8z3L9UtyxyZDKMrSdLy8AeQAuyBNdvv/mpynOhRqPTOnK4aHZDi4W4TfgSxBsfEDZAJ1zpnMElSVjC5Fdzbc9jodOj3bn6CTseVmkfUsq+yqzugEx4i/sLYg4/JHyytwHuiFebskgEBQCT9GNlqCF2+wKzTpUqNZAK8tyHM6r7blDKaDFTw3n8gAAAAAhiP8Uau/R8wABrgKAUAAAqG9mG7HEZ/sCAAAAAARZWg=='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
