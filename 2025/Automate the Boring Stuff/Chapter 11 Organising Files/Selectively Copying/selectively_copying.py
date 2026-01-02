"""
Selectively copy files with .src extension from one folder to another
"""
import os, shutil
from pathlib import Path

def copy_selected(source, destination, extension="*"):
    source_path = Path(source)
    destination_path = Path(destination)

    # validate source directory
    if not source_path.is_dir():
        raise ValueError(f"{source_path} is not a valid directory")

    # validate desitantion directory
    if not destination_path.is_dir():
        os.makedirs(destination_path)

    def ignore_files(dir, files):
        return [f for f in files if os.path.isfile(os.path.join(dir, f)) and not f.endswith(extension)]

    shutil.copytree(source_path, destination_path, 
                    ignore=ignore_files, dirs_exist_ok=True)
    
if __name__ == "__main__":
    s = r"C:\Users\Eem\Documents\Python\mooc-fi-data-analysis-2024-25"
    p = r"C:\Users\Eem\Documents\Python\misc-python-scripts\2025\Automate the Boring Stuff\Chapter 11 Organising Files\Selectively Copying\Copied_files"
    e = (".py", ".txt", ".csv", ".tsv")

    copy_selected(s, p, e)