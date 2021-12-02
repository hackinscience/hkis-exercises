# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AM9dABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9Z8KqXJoAerAd9lwEAuSOQyyLHKJcx2mLmDZnV+VSRoP5nOQBWYJKi+Hc6E1hlG7PvumICD/4rsSmkts25uH9FZ9l/0q+HYsMpmtnyBJVDGiS9plP2R1KTG92zApzdyJhaAde/bzpz3D1Krwi1WC20ulj0Kzs63rHuGNzn2TkdVAAlHnUkZHSm4cllwNtAAAAy94ZnN0M43UAAesBgFAAAKeOUwOxxGf7AgAAAAAEWVo='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
