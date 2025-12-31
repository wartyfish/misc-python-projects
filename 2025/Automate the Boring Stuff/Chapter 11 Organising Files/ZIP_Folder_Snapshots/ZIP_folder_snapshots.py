"""
ZIP snapshot generator.

Program backs-up selected folder to a new ZIP folder each time it's run.
"""
import os, zipfile
from pathlib import Path

def compress_to_zip(folder_name, target_dir):
    folder_path = Path(folder_name)
    target_path = Path(target_dir)

    # create target directory if it doesn't yet exist
    if not target_path.is_dir():
        os.makedirs(target_path)

    # get new snapshot path
    i=0
    while True:
        zip_name = f"snapshot_{i:03}.zip"
        p = target_path / zip_name
        if p.is_file():
            i+=1
        else:
            break

    # create new snapshot to p
    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as zipobj:
        for file_path in folder_path.rglob("*"):
            if file_path.is_file():
                zipobj.write(file_path, arcname=file_path.relative_to(folder_path))

compress_to_zip("Test_folder", "snapshots")