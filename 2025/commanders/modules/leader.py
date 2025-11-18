import re

class Leader:
    def __init__(self, rank, name, DOB, DOD, nation, greatest_acheivement):
        self.rank = rank   
        self.name = name
        self.DOB = DOB
        self.DOD = DOD
        self.nation = nation
        self.greatest_acheivement = greatest_acheivement
        self.name_and_rank = f"{self.name} ({self.rank})"

        # seperate country from dynasty where applicable
        pattern = r'(.+?)\((.+?)\)'
        if match := re.match(pattern, self.nation):
            self.nation = match.group(1).strip()
            self.dynasty = match.group(2)
        else:
            self.dynasty = None
    def __str__(self):
        #str_DOB = str(self.DOB).strip("-")
        #if self.DOB < 0:
        #    str_DOB += " BC"
        #str_DOD = str(self.DOD).strip("-")
        #if self.DOD < 0:
        #    str_DOD += " BC"
        return f"{self.rank:3}. {self.name} ({self.DOB}–{self.DOD}, {self.nation})" 
    
