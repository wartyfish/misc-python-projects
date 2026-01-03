import os, shutil
from pathlib import Path

def make_gaps(target):
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

    def file_plus_one(file):
        file_no = int(file.name.strip("spam").strip(".txt"))
        return f"spam{file_no+1:03d}.txt"

    def find_next_file(file):
        next_file = p / file_plus_one(file)
        if os.path.isfile(next_file):
            return next_file
        else:
            return find_next_file(next_file)

    number_of_files = len([f for f in p.iterdir()])
    print(number_of_files)
    i = 0
    while True:
        if i == number_of_files:
            break
        for f in p.iterdir():
            i += 1
            if i == number_of_files:
                break
            f_plus_one = p / file_plus_one(f)
            if not os.path.isfile(f_plus_one):
                next_found_file = find_next_file(f)
                os.rename(next_found_file, f_plus_one)
                i = 0
                break

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
    make_gaps(p)
    fill_gaps(p)
    

if __name__ == "__main__":
    main()