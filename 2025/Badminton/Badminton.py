import gspread
from google.oauth2.service_account import Credentials
import datetime
from badminton_stuff.session import Session
from badminton_stuff.participant import Participant

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(r"C:\Users\jamie\OneDrive\Desktop\Python\Badminton_API\credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet = client.open("Badminton Session Log").worksheet("Log")
processed = client.open("Badminton Session Log").worksheet("Processed")

# stores session-type objects, key = date (string rep)
sessions = []
# stores player-type objects, key = name
players = []

# Pulls data from the spreadsheet, formats each line
# Creates a new Session object for each session
def read_from_sheet():
    data = sheet.get_all_values()
    
    # ['Date', 'Who booked?', 'Who played?']
    headers = data[0][0:3]
    rows = [value[0:3] for value in data[1:]]

    # strips any empty rows
    rows = [row for row in rows if any(cell.strip() for cell in row)]

    # Extracts the date, and the names of the players who played and who booked (if applicable)
    # Passes these to new_session method which converts players to Participant objects 
    # and appends new Session object to sessions
    for row in rows:
        date = row[0]
        played_names = row[2].split(", ")

        if row[1].strip() == "":
            create_new_session(date, played_names)
        else:
            booked_names = row[1].split(", ")
            create_new_session(date, played_names, booked_names)
    
    for session in sorted(
        sessions,
        key = lambda s: s.date_datetime
    ):
        update_player_attributes(session)

def create_new_session(date: str, played_names: list, booked_names: list=None):
    if booked_names == None:
        booked_names = []
    # create player object for any new players
    for player in played_names:
        if player not in [p.name for p in players]:
            players.append(Participant(player))

    played = [player for player in players if player.name in played_names]    

    for player in booked_names:
        if player not in [p.name for p in players]:
            players.append(Participant(player))
    
    booked = [player for player in players if player.name in booked_names]
    if booked == None:
        booked = [""]

    new_session = Session(date, played, booked)
    sessions.append(new_session)
    return new_session        
    
def update_player_attributes(session: Session):
    # check if anyone is booking, and if not, find two players who are next to book
    if len(session.who_booked) == 0:
        to_book = [
            player for player in sorted(
                session.who_played,
                key = lambda p: (-1 * p.sessions_since_last_booking, p.bookings_per_session)
            )
        ][:2]
        for player in to_book:
            player.due_to_book = "yes"
    
    # if player(s) have already booked, proceed as normal
    else:
        for player in session.who_played:
            player.times_played += 1
            player.sessions_played.append(session.date_datetime)
        
        for player in session.who_booked:
            player.times_booked += 1
            player.sessions_booked.append(session.date_datetime) 

def update_log_sheet():
    # Clear table range
    sheet.batch_clear([f"A2:C1000"])

    # Ensure sessions are sorted reverse chronologically
    sessions_sorted = sorted(
        sessions,
        key = lambda p: p.date_datetime,
        reverse = True
    )

    rows = []
    for session in sessions_sorted:
        rows.append(
            [session.date, 
            ", ".join(sorted([p.name for p in session.who_booked])), 
            ", ".join(sorted([p.name for p in session.who_played]))]
        )  

    # If no one yet booked, write data from A2
    if len(sessions_sorted[0].who_booked) == 0:
        sheet.update(values=rows, range_name="A2")
    # Otherwise, write data A3
    else:
        sheet.update(values=rows, range_name="A3")

def build_processed_sheet():
    rows = []
    for player in sorted(
        players,
        key = lambda p: (-1 * p.sessions_since_last_booking, p.bookings_per_session)
    ):
        rows.append(
            [
                player.name,
                player.times_played,
                player.times_booked,
                player.sessions_since_last_booking,
                round(player.bookings_per_session, 2),
                player.due_to_book,
            ]
        )
    
    print_processed(rows)
    return rows

def update_processed_sheet():
    # Clear table range
    processed.batch_clear([f"A2:F"])   
    rows = build_processed_sheet() 
    processed.update(values=rows, range_name="A2")

def print_rows():
    print(f"Date{" "*4}|Booked{" "*9}|Played")

    for session in sorted(
        sessions,
        key=lambda p: p.date_datetime,
        reverse=True
    ):
        who_booked = ", ".join(player.name for player in session.who_booked)
        who_played = ", ".join(player.name for player in session.who_played)

        print(f"{session.date}|{who_booked:15}|{who_played}")

def print_processed(rows: list):
    print(f"{" "*10}|{"Sessions".center(15)}|{"Sessions".center(15)}|{"Sessions since".center(15)}|{"Bookings per".center(15)}|{"Due to".center(10)}")
    print(f"{"Name".center(10)}|{"played".center(15)}|{"booked ".center(15)}|{"last booking".center(15)}|{"session".center(15)}|{"book?".center(10)}")

    for row in rows:
        print(f"{row[0]:9} |",end="")
        print(f"{row[1]:14} |",end="")
        print(f"{row[2]:14} |",end="")
        print(f"{row[3]:14} |",end="")
        print(f"{row[4]:14} |",end="")
        print(f"{row[5]:>9}")        

def input_new_session():
    date = input("Date (dd/mm/yy): ")
    print("Enter who played, comma seperated:")
    who_played = input() 
    try:
        who_played = who_played.split(", ")
    except: 
        who_played = [who_played]

    suggested = ", ".join([player.name for player in players if player.name in who_played])
    
    print(f"Enter who booked, if applicable, comma seperated:")
    print(f"Suggested to book: {suggested}")
    who_booked = input()
    
    if len(who_booked) > 0:
        try:
            who_booked = who_booked.split(", ")
        except:
            who_booked = [who_booked]
    else:
        who_booked = []
    
    new_session = create_new_session(date, who_played, who_booked)
    update_player_attributes(new_session)
    
    print("New session added:")
    print()
    print_rows()


read_from_sheet()
print_rows()
print()
build_processed_sheet()
print()

input_new_session()
build_processed_sheet()
print()

if input("Update spreadsheet? [y/n] ").lower() == "y":
    print()
    update_log_sheet()
    print("Log sheets updated successfully")
    print_rows()
    print()
    update_processed_sheet()
    print("Processed sheet updated successfully")
