import gspread
from google.oauth2.service_account import Credentials
import datetime

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet = client.open("Badminton Session Log").worksheet("Log")
sessions = {}
players = {}

class Player:
    def __init__(self, name: str):
        self.name = name
        self.times_played = 0
        self.times_booked = 0
        self.time_since = -1
        self.sessions_booked = []
        self.sessions_played = []        
        self.due_to_book = ""

    @property
    def bookings_per_session(self):
        if self.times_played == 0:
            return 0
        else:
            return self.times_booked / self.times_played
    
    def __str__(self):
        return f"{self.name:6} Sessions played: {self.times_played:2}, Sessions booked: {self.times_booked:2}, Sessions since last booking: {self.time_since:2}"
    
    # record booking
    def booked(self, date):
        self.times_booked += 1
        self.time_since = 0
        self.sessions_booked.append(date)

    # record session played
    def played(self, date):
        self.times_played += 1
        if self.time_since == -1:
            self.time_since = 0
        self.time_since += 1
        self.sessions_played.append(date)

def read_from_sheet():
    data = sheet.get_all_values()
    
    # ['Date', 'Who booked?', 'Who played?']
    headers = data[0][0:3]
    rows = [value[0:3] for value in data[1:]]

    #converts dd/mm/yyyy strings to date objects that can be sorted (reverse) chronologically
    def parse_date(d):
        try:
            return datetime.datetime.strptime(d, "%d/%m/%y")
        except ValueError:
            return datetime.datetime.min
    
    rows.sort(key=lambda r: parse_date(r[0]), reverse=True)
    rows = [row for row in rows if any(cell.strip() for cell in row)]
    
    # store parsed rows for later processing
    # parse rows in chronological order (reverse order to how their stored in the "Log")
    rows_reversed = rows[::-1]
    
    for row in rows_reversed:
        parse_line({'Date': row[0], 'Who booked?': row[1], 'Who played?': row[2]})    
  
    return headers, rows

# receives each line as a dictionary:
# line['Date'] = [date]
# line['Who booked?'] = ['p1', 'p2']
# line['Who played?'] = ['p1', 'p2'... 'p8']
def parse_line(line):
    date = line['Date']
    sessions[date] = {}
    sessions[date]['booked'] = [name.strip() for name in line['Who booked?'].split(",")]
    sessions[date]['played'] = [name.strip() for name in line['Who played?'].split(",")]
    sessions[date]['not booked'] = False

    # If "Who booked?" value empty and "Who played?" not empty:
    # Do not update player objects. Instead, denote session as not booked
    if sessions[date]['booked'][0] == '':
        if sessions[date]['played'][0] != '':
            sessions[date]['not booked'] = True
            for name in sessions[date]['played']:
                if name not in players:
                    players[name] = Player(name)

    else:
        for name in sessions[date]['played']:
            if name not in players:
                players[name] = Player(name)

            players[name].played(date)
        
        for name in sessions[date]['booked']:
            players[name].booked(date)

# updates table in log sheet
# entries sorted reverse chronologically, with an empty row below headers
def update_log_sheet(headers, rows):
    num_rows = len(rows) + 2 #+1 for blank row
    num_cols = len(headers)

    # Clear table range.
    # chr() converts int to unicode character
    # ASCII code 65 is 'A', so 64 + num_cols converts number to letter of row in spreadsheet
    # ie chr(65) = 'A', chr(66) = 'B', etc...
    sheet.batch_clear([f"A2:{chr(64 + num_cols)}{num_rows+10}"])

    # Write data starting as A2
    sheet.update(values=rows, range_name="A3")

def update_processed_sheet():
    players_formatted = []

    for date in sessions:
        if sessions[date]['not booked'] == True:
            players_in_booking_session = sessions[date]['played']
            sorted_players = sorted(
                players.values(), 
                key = lambda p: (p.time_since, -1 * p.times_booked), 
                reverse = True
            )

            eligable = [p for p in sorted_players if p.name in players_in_booking_session][:2]

            for player in eligable:
                player.due_to_book = "Yes"

    for player in sorted(players.values(), key=lambda p: (p.time_since, -1 * p.bookings_per_session), reverse=True):
        players_formatted.append([player.name, player.times_played, player.times_booked, player.time_since, round(player.bookings_per_session, 2), player.due_to_book])

    processed = client.open("Badminton Session Log").worksheet("Processed")
    processed.clear()
    processed.update([["Name","Sessions played","Sessions booked","Sessions since last booking","Bookings per session","Due to book?"]] +
                    [line for line in players_formatted])
    print("Data written successfully")

headers, rows = read_from_sheet()
update_log_sheet(headers, rows)
update_processed_sheet()

print(rows)

