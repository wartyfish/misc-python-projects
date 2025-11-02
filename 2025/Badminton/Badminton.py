import csv

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
        return f"{self.name:6} Sessions played: {self.times_played:2}, Sessions booked: {self.times_booked:2}, Sessions since last booking: {self.time_since:2}, Bookings per session played: {self.bookings_per_session:.2g}"
    
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

# Reads badminton-log CSV ("Date", "Who booked?" (comma-deliniated names), "Who played?" (comma-deliniated names))
# Adds new value to the sessions dictionary with the key being the date and the value being another dictionary.
# sessions[date] has two values, "booked" and "played".
# New players are automatically created and added to players dictionary.
# If "Who booked?" cell is empty, next_to_book is populated with the two players with the most games played per booking,
# and the lowest bookings/session played ratio
def parse_line(line):
    date = line['Date']
    sessions[date] = {}
    sessions[date]['booked'] = [name.strip() for name in line['Who booked?'].split(",")]
    sessions[date]['played'] = [name.strip() for name in line['Who played?'].split(",")]

    # If "Who booked?" value empty, assume session has not yet commenced.
    # Do not update player objects. Instead, inform user who is next to book. 
    if sessions[date]['booked'][0] == '':
        sorted_players = sorted(
            players.values(), 
            key = lambda p: (p.time_since, -1 * p.times_booked), 
            reverse = True
        )

        eligable = [p for p in sorted_players if p.name in sessions[date]['played']][:2]

        for player in eligable:
            player.due_to_book = True
            print(player.name,"due to book")

    else:
        for name in sessions[date]['played']:
            if name not in players:
                players[name] = Player(name)

            players[name].played(date)
            print(players[name].name, "played on",date)
        
        for name in sessions[date]['booked']:
            players[name].booked(date)
    
def print_players():
    for player in sorted(players.values(), key=lambda p: (p.time_since, -1 * p.bookings_per_session), reverse=True):
        print(player)

# Goes through all players, sorts by times since their last booking, and their bookings/sessions ratio.
# Saves data "Processed.csv"
def output_data():
    players_formatted = []
    for player in sorted(players.values(), key=lambda p: (p.time_since, -1 * p.bookings_per_session), reverse=True):
        players_formatted.append([player.name, player.times_played, player.times_booked, player.time_since, player.bookings_per_session, player.due_to_book])

    with open("Processed.csv", "w") as f:        
        f.write("Name,Sessions played,Sessions booked,Sessions since last booking,Bookings per session played,Due to book?\n")
        for player in players_formatted:
            line = ""
            for value in player:
                line += f"{value},"
            line = line[:-1]
            f.write(line+"\n")
    
    print("Data written to Processed.csv")

def plan_session(list_of_players: list):
    ordered_names = []
    for player in list_of_players:
        if player not in players:
            players[player] = Player(player)
            
    for player in sorted(players.values(), key=lambda p: (p.time_since, -1 * p.times_booked), reverse=True):
        if player.name in list_of_players:
            ordered_names.append(player)

    for p in ordered_names:
        print(p)
            


with open ("Log.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        parse_line(row)

#print_players()
output_data()


#names = ["Gabe", "Paddy", "Oscar", "Jamie", "Max"]
#plan_session(names)