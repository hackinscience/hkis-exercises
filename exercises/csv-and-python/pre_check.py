# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AfxdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9Zs4FJeO7ZicZisiN1ZBFJc+wKuAOgQvMV0TrsgsxfyUxlTKuxQgpanzV4urKmWWeTf1puo1Ajjf5Yz4PRO6LImtTYmk8gkocnj0Wq6zeesmYXy5mLNg+NjhomWrQfCJu8vTN7Ytr5Vy4yt3XzFq0mPBRmSXG8FblgCnmMJ9UOisrNYziK/ozlIDcJmjwYEq8+3A0Oq+qv3N0qrmAScmNRre5mZRibG6J8fD9NUcy5PfIPRgdGp2BE3ml3Lj/6K71P9JjNlOhCl92dkwgF2GIXqIvxZBVQNDl980Qu61svQ/0nNxKEmSt4TdXDKyug+wYyZCDYKEaPH7JD5mWixZZN8ImtyoDplVRlih4GdXrjTgGt+Kcsu96P7d3p3ugY5/96Q6lbe3Cbb58gOZTXJeqYJZikB51qeLDSV0kOI0xaL0K1kZ+lHzlDK4EOrtPmPh7Kise/F5OX5DxkmpxtdPUCaIKOT8a/3xM79RGpdnBYajCN9mjbpW5oPBYgflLAYFaVGQgY553AJqvejsgmmMTUzRj9lAPEHenuJ/rroxAqGi1lQwmdKnhfSToyk9b6rN+XyfQDzsUaLIBbgAAsyAPLiqWF9QAAZgEgFAAALh+BUaxxGf7AgAAAAAEWVo='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
