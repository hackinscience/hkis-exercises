# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AfRdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9Zs4FJeO7ZicZisiN1ZBFJc+wKtxhY1wdpXS763nOl8viPAeO0zhASIV10Iarf73JZ7z9AFz/cBkby6Twg8hiWKyX8X+Wr3DznnnTERCHR0IoguD4Ft6zQoKLT4H0FB4YxttDkk/1b6xgq6oesq8aJ7NnrOa3PIm/9FGN3jkOL29gYcjE4h2+DN6c9b36kCPj8SZ5762Rcn5LDPrMAMK+vX6c+rMy93wyyMdiSkGc1lXTrTOr2JHDJSdWPngJ6+HHjUkovimULH3unnamwT2bJBGfDLro7zk3gXC4ty3Qjk3PXC9RvMz369vpNH4p1avFAqiNrrU/QD/jHT+PKpBjIeV5HQQ9deW5aZvMOZGvbrYLIRH9RA5UxFYb0/Pnvd5azw0T+CLs5hGUDMDdXFuCaeWhsBR4MxBqJUTaA6m/x9Lwblokc6pveSyhNgrfzXD1LSFZhMhGT7wuNbEtx5rSAa6GA8UaK263MzWzETFPzqFEt59SLpDeIy0k8oiNa9PsZUQzin28piF2221SVZoRsXoKiRkwOMmLpflUXk6qxXQyMxQhC27Tz/93FMTvWn01MukAAIwu7GXKn9uZAAGQBIBQAADV/FaqscRn+wIAAAAABFla'))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
