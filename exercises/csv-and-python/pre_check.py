# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AgFdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9Zs4FJeO7ZicZisiN1ZBFJc+wKtxhY1wdpXSy1Omc5JkdCb5gWOa/kzR/TS3Y9BNvs0ykRkOfbpwvOIhIgETOrlaHGvG+hIAibmqQ8HKQae1D8CgdvWqVOhkDF9/ce7lHGGd7+eF2Z1CM2XqHwDGarLoCKNnoc4iveKhjALSwMHrNJDsx7koO+2E9bg8d8TR4g/2tO52/fqXAJNNZL5NCYDjrv1zaZ8oLKOrXy1Nrt4svSip9QXVYYJ2/GZimx5F4sLhL42wCMYiKsiTvuIE8txl9lwLdM5ZeeK8pyCTNIMfFpAolfjBKyj8cQZc9DgXMP6bt9LpvrgeobdYrOZenh6Qzx+hC4bRm9mLKUTWlqgdL3u3Qigepu6G1Z2iFI9NpIWdu002K8DBYbpb2r13vfXhZEh3DqoASX8uafXtRDvMx1UZEWT4u8M59c44q8KUDjKTXSK2SGOj4EmQ5N6li18UAy6tfpz3mDb/fB+eL/twU99Iq5dUe9L/qun4iMOmO5LGs/POjbCHZV3PrDSylRwHAwuUK7nKgZj10G6vCMSVt0DFCR3/722aRDPwyNy0qE7H3IuHzVUZU1Db2TFZjAAAAAACN3eCQudel4AABnQSAUAAAC+/IFrHEZ/sCAAAAAARZWg=='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
