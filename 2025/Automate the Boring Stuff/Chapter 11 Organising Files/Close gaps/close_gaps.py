import os
from pathlib import Path

def make_gaps(target):
    p = Path(target)
    if not p.is_dir():
        p.mkdir()
    for i in range(200):
        if i not in (3, 54, 69, 102, 103, 197):
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
            print(f"Next file: {next_file}")
            return next_file
        else:
            find_next_file(next_file)

    for f in p.glob("*"):
        if f == p / "spam199.txt":
            break
        f_plus_one = p / file_plus_one(f)
        if not os.path.isfile(f_plus_one):
            print(f"{file_plus_one(f)} missing")
            print(f"Next file: {find_next_file(f)}")
        
        


def main():
    p = r"misc-python-scripts\2025\Automate the Boring Stuff\Chapter 11 Organising Files\Close gaps\Files"
    if True:
        make_gaps(p)
    fill_gaps(p)
    

if __name__ == "__main__":
    main()