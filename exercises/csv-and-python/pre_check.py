# AUTO GENERATED: DO NOT EDIT.
from pathlib import Path
import io
import tarfile
import base64
import lzma
from subprocess import run

tar_bytes = io.BytesIO(base64.b64decode(b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4Cf/AbtdABcLvBx9AZXAMzmZXGs1sHxm1kMiRwkeeBumwiMg004DOoE/QcYZlp2py5lQ5+6m1liL/vSdp+3pa3QzqPz4eiWhQB/l4mym2YniNUE9pyq8h2mV6hxuz6CwAZR9wiq/Gh7mDpqNXFnSJioTQmC4mZdCuxPQH6xnOt7V7Ny6ACIdhIXDoR4FrCGghVgqo2y8WLuMYHekBjtAkdtxL3KL+ovVrWi2PtFnvg9FpaSJ7+TQm03Z3PlFL55zf1SyfE8EP9wITHHLea9jQILFhnvnDmflUUs3HPQldWvcPqN+c6Va/o/TWGcHWbT7IsH5eYgbr1YGOBs2OBXGfp83wT+/5xSdI/iBNAZpVPO6wnzTJg+DP7zeVEito4MP+suAwjA7aOI28MxDDc+5efv6lJzBVICViz3ZExgQ7Tk9cbGt8Wdf1TLlz/ynERLhVbYTai5Ms6cbTkqDgagN/46mRisXs0a4PzRrdehJpo8GGdM7HsuRPRyuqPVAQOuSmD1UkZny5920wwzPSxIrz1fGnoDiVy8rispQvSe9e9FWGqYS9Uhe7qbeAiwNFgRk6rqVf+/8vNeXol+nPya+pC4AAABjmSP6wrnlAQAB1wOAUAAAERorCrHEZ/sCAAAAAARZWg=='))
with tarfile.open(fileobj=tar_bytes, mode="r:xz") as t:
    t.extractall(".")

if Path("solution").exists():
    Path("solution").rename("solution.py")
