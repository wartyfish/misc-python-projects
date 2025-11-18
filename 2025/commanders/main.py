from modules.leader import Leader
import re

def read_text():
    pattern = re.compile(
        r'^\s*'                 # New line, including any whitespace
        r'(.+?)\s\t'            # 1. rank
        r'(.+?)\s\t'            # 2. name
        r'(.+?)\s\t'            # 3. DOB
        r'(.+?)\s\t'            # 4. DOD
        r'(.+?)\s\t'            # 5. nation
        r'(.+)'                 # 6. greatest acheivement

    , re.UNICODE | re.IGNORECASE
    )

    leaders = {}
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        for line in f:
            if match := pattern.search(line.strip()):
                rank = int(match.group(1))
                name = match.group(2).strip()
                dob = match.group(3).strip()
                dod = match.group(4).strip()
                nation = match.group(5).strip()
                greatest_acheivement = match.group(6).strip()
                

                try:
                    leaders[name] = Leader(rank, name, dob, dod, nation, greatest_acheivement)
                except:
                    print("Failed to parse:",line)
    return leaders  


def main():
    leaders = read_text()
    print(len(leaders))
    nations = {}
    for leader in leaders:
        if leaders[leader].nation not in nations:
            nations[leaders[leader].nation] = [leaders[leader].name_and_rank]
        else:
            nations[leaders[leader].nation].append(leaders[leader].name_and_rank)

    with open("processed.txt", "w", encoding="utf-8") as f:
        for leader in leaders:
            f.write(f"{leaders[leader]}\n")
    
    with open("sorted_by_nations.txt", "w", encoding="utf-8") as f:
        for nation in sorted(nations, key=lambda n: len(nations[n]), reverse=True):
            leaders = ", ".join(leader for leader in nations[nation])
            f.write(f"{nation} ({len(nations[nation])}): {leaders}\n")      
        


if __name__ == "__main__":
    main()
