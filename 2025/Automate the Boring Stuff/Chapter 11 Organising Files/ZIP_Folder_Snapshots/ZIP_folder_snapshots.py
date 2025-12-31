"""
ZIP snapshot generator.

Program backs-up selected folder to a new ZIP folder each time it's run.
"""

import os, zipfile
from pathlib import Path

# get new snapshot path
i=0
while True:
    zip_name = f"snapshot_{i:03}.zip"
    p = Path("snapshots") / zip_name
    if p.is_file():
        i+=1
    else:
        break

# create new snapshot to p
with zipfile.ZipFile(p, "w") as z:
    z.write("Test_folder", compress_type=zipfile.ZIP_DEFLATED)
