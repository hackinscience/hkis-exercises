# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/ANldABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9Z8KqXJoAerAd9lwEAuSOQyyLHKLELlR54S6HNbfLaXK/JN3dQurh9qdOw3sbVeJ5fd93O1uaJGO+X0MAOLR0ZhbNsS1ngBNC7JortT1+ayV3RRnJ/Qps6IcSIpqbeDgtfewL0r79CFT4XEt3cgMFVrPiczFVhKKxsHLq4IoFRPwRRNlsplMYy5e/iVnuzqX/7uInbZHlmAoAAAAAJDOyVqvHXjQAAfUBgFAAAEztjzqxxGf7AgAAAAAEWVo='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
