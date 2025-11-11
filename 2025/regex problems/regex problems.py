import re

# Match specific words
s = "The cat sat on the cathedral."
print(re.findall(r'\bcat\b', s))

# Case-insensitive match
s = "Hot dog hot Dog hot diggedy dOG - snoop dogg"
print(re.findall(r'\bdog\b', s, re.IGNORECASE))

# Digits only
s = "Room 12 costs 30 quid"
print(re.findall(r'\d+', s))

# Word boundaries
s = "The carpet in the car needs a clean."
print(re.findall(r'\b[Cc]ar\b', s))

# Find punctuation 
s = 'In a statement, NUJ general secretary Laura Davison says the next director general must be "politically independent" and able to face pressures, including "AI-supercharged fake news".'
import string
print(re.findall(r"[.,'\"]", s))

# Find emails
s = 'Alice: alice@gmail.com, Bob: bob29@yahoo.co.uk, Charlie: chazzer_420@protonmail.org'
print(re.findall(r"[\w\.-]+@[\w\.]+\.\w+", s))

# Phone numbers
s = 'Alice: +44712123123, Bob: 07 456 456 465, Charlie: 07-789-789-789'
print(re.findall(r'(?:\+44|07)(?: *|-)\d\d\d(?: *|-)\d\d\d(?: *|-)\d\d\d\b', s))

# Alternation
s = 'The Cat brown mouse dogged over the slow brown dog with a mouse in its cat'
print(re.findall(r'\bcat\b|\bdog\b|\bmouse\b', s, re.IGNORECASE))

# Capturing groups
s = "My birthday is on 2025-11-10"
print(re.findall(r'(\d{4})-(\d{2})-(\d{2})', s))

# Extract hashtags
s = "I love #Python and #Machine-Learning, but #regex can be tricky."
print(re.findall(r"\#[\w-]+", s))

# Date extraction 2
s = "John was born 28/10/2000 and Jane was born 01/01/1970"
print(re.findall(r"(?:[012]\d|3[01])/(?:[0]\d|[1][0-2])/[012]\d{3}", s))

# Find capitalised words
s = "Alice and Bob went to NewYork in July."
print(re.findall(r"\b[A-Z][a-z]*\b", s))

# Extract repeated words
s = "I want to to go to the the park."
print(re.findall(r"\b(\w+)\s+\1\b", s))

# Extract all quoted text
s = 'He said "Hello" and then she replied \'Hi there\'.'
print(re.findall(r"[\"\'](.*?)[\"\']", s))

# Extract conditional statements
s = "If it rains, then we stay. If it snows, then we go."
print(re.findall(r"[Ii]f (.*?), then", s))

# Lookahead/lookbehind
s = "Don't include 1 but do include numbers %2 %34 and %5. Don't include plurals or any other words ending in s."
print(re.findall(r"(?<=%)\d+", s))                                  # positive lookbehind
print(re.findall(r"(?![a-z']*s\s)\b[a-z']+\b", s, re.IGNORECASE))   # negative lookahead
#print(re.findall(r"\b[a-z']+[^s\W]\b", s, re.IGNORECASE))

# HMTL tag extraction
s = "<title>example text</title>"
print(re.findall(r"<title>(:?.*)</title>", s))

# Named groups
s = "Name: John Doe, Age: 30"
pattern = r"Name:\s(?P<first>\w+)\s(?P<last>\w+)"

match = re.search(pattern, s)
if match:
    result = match.groupdict()
    print(result)

# Extract URLs
s = "Visit https://example.com or http://test.co.uk for info."
print(re.findall(r"\bhttp[s]*://\w+[\.\w+]+\b", s))

# Validate passwords (8+ char and contains at least: one upper, one lower, one digit one special character):
s = "p1: Abcdef1! p2: MyP@ssword123 p3: Z9x$wQ7r p4: Happy#2025 p5: abcdefg1 p6: ABCDEFG1! p7: Abcdefgh! p8: Abcdef12 p9: A1!b p10: Aa1_aaaa"

pattern = r"(?P<p_num>p\d+):\s(?P<p_pass>[^\s]+)"

passwords = {}
for match in re.finditer(pattern, s):
    passwords[match.group("p_num")] = match.group("p_pass")
print("All passwords:  ", passwords)

valid_pass_pattern = r"((?=\S{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?])\S+)"
valid_passwords = {}
for p in passwords:
    valid = re.match(valid_pass_pattern, passwords[p])
    if valid:
        valid_passwords[p] = passwords[p]
print("Valid passwords:", valid_passwords)

# Log file parsing
s = "[2025-11-10 14:32:21] ERROR: Connection failed"

print(f"{"Timestamp:":10}", re.findall(r"\[(.*?)\]\s", s))
print(f"{"Type:":10}", re.findall(r"(?<=\]\s)(\w*):", s))
print(f"{"Message:":10}", re.findall(r"(?<=:\s)(\w*)\b", s))