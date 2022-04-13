# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/ANJdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9aDo+XtwI2qf5PLhgG85YJynwzcseoyTiq3Yf3ImEKEsnsL428Hh7cT7+dp6Hv66VM7wur6dZwnSz3NyHbyDQmvAPeqZ7y5h5a8XR3IiqhQUlyZCkiYmO6OBs2IbR70JEg6szCAqOF/w01Mjy8c6P1viUWabIqVK8nG9mAb350dvyjN6b2NGd9RbZdZqmST8zAAAAAA3GGuACA7ptAAHuAYBQAAAUH55TscRn+wIAAAAABFla'))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
