# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AwBdABcL3ASAUDIm7h19G/PyyzPs7Pg38OrWet04dhtWH3Vustl6lPJpZ0H2EkjpO96jLtkR94wkbpcbQqvHv3cBENx9Zs49qYCDWOwztCV6ecOEye2iFXDsyL5vhWIcci+9cJsSab0YJeNeV3kPXI5ZiBs+osg5ZgvdGf7Io9JbLTM86dGuHVCQ0o027qfd8PDa/BmkoD3laKqRdsjWAmGs3iMiOupNoxBraBX+TRchCAQPNShi13nL8xXe0tOxAOPAf3gsgcLFv1cnJNoht30pd39P2JhfpUkdvBu6yTlUzyqbOHMoYnPtb8dciDaHzEJfWwyL4xGF1EB9szYfvIRvoXZy7eaF549Je9aTGi+uW1hxgaXwvHrZ8VjdZoIxTU0WqCSTHJ3JL8E7gZ8gi9YZgxfnKoOikfYDwhBruOiR+WJJGjyrNZcSZzgGsHwLOxwIkYbTntW/HMQukKlShqxk0eNPkfudt8AX1O9SPZkK0yHzbeNYVHzPWyKIoL/z5pVeirMR5kzslQUO0Lwh1sDCPYAEH/SSPnC4rqPTUuPZnMvXA8WDrn6BHGlEXwjNMNtsgDdGpxYdHuKMYDKXdz8pzdpugEIAZqqJf+cuT1T7Xa+y2kSJRyDcvvGV6Gr8ZirkTllH7R0PATC0w+y8N7eX5517btpZMT/jdjZ+qHXX+CbnmUsRob5F60tFm0ag6ECNbD0McLAP6ePHIaOUbhb2MrG6n4gtF7pBuQ+pI8zy0NLhxs2Won5pkmzyNflaRKJq8ZCOaopdJFjJ+5gjnMXWvK7GX1vOzAG421J2rpr8BMGrbVEIvB0ssvnrhPBdznR7EI8oVXowrSJXXdIkadW4HJdbZYmq+vTpRdnnQqzNOatMSdr+BQM/WOFJexG+PEt3HY6FO2tBTMM6qfnnxK+P4PVn1ajiwcUV3DG3EpwZ7ZnS1qgub3WjGbK6ibZVf/nUmWAuDRP4cS0uTEJ2+EstgcWh0Frz37ICL2lmIiEQzWW0zZlSEaDCnhm5Mf/CRREmAADWNt9ltdGIjgABnAaAUAAAzm9Up7HEZ/sCAAAAAARZWg=='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
