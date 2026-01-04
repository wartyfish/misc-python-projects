"""
Close gaps

make_files function populates "Files" directory with numerically names "spamXXX.txt" files, with specified gaps in file numbers.
 
"""

import os, shutil, re
from pathlib import Path

def make_files(target):
    p = Path(target)
    if not p.is_dir():
        p.mkdir()
    for i in range(11):
        if i not in (3, 5, 7):
            f = p / f"spam{i:03d}.txt"
            with open(f, "w") as file:
                pass

def fill_gaps(target):
    p = Path(target)
    pattern = re.compile(r"spam(\d{3}).txt")

    # populate dict that indexes filenumbers
    indexed_files = {}
    i = 0
    for f in p.iterdir():
        file_index = f"{i:03d}"
        valid = re.match(pattern, f.name)
        if valid:
            indexed_files[file_index] = f
        i += 1
    
    # identify files that need to be renamed and then do so
    for i in indexed_files:
        if i != re.match(pattern, indexed_files[i].name).group(1):
            new_name = re.sub(r"\d{3}", i, indexed_files[i].name)            
            os.rename(indexed_files[i], p / new_name)
            print(f"{indexed_files[i].name} renamed to {new_name}")

def make_gaps(target, gaps=list):
    p = Path(target)
    pattern = re.compile(r"spam(\d{3}).txt")

    # as before, populate dict with indexed filenumbers
    # this time with specified gaps
    indexed_files = {}
    i = 0
    for f in p.iterdir():
        # generate file indices with gaps
        while i in gaps:
            i += 1
        
        file_index = f"{i:03d}"
        valid = re.match(pattern, f.name)
        if valid:
            indexed_files[file_index] = f
        i += 1

    # identify files to be renamed, this time working in reverse order
    for i in reversed(indexed_files):
        if i != re.match(pattern, indexed_files[i].name).group(1):
            new_name = re.sub(r"\d{3}", i, indexed_files[i].name)          
            os.rename(indexed_files[i], p / new_name)
            print(f"{indexed_files[i].name} renamed to {new_name}")
        


def delete_files(target):
    p = Path(target)

    for f in p.iterdir():
        if f.is_file() or f.is_symlink():
            f.unlink()
        elif f.is_dir():
            shutil.rmtree(f)

def main():
    p = r"misc-python-scripts\2025\Automate the Boring Stuff\Chapter 11 Organising Files\Close gaps\Files"
    
    delete_files(p)
    make_files(p)
    fill_gaps(p)
    gaps = [2, 4, 6, 8]
    make_gaps(p, gaps)
    

if __name__ == "__main__":
    main()