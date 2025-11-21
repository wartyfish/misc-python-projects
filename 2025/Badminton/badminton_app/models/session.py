# A record of each session info (date, who played, who booked)
import datetime

class Session:
    def __init__(self, date: str, who_played: list, who_booked: list = None):
        self.date = date
        try:
            self.date_datetime = datetime.datetime.strptime(self.date, "%d/%m/%y")
        except ValueError:
            print("ValueError: failed to assign datetime")
            self.date_time = datetime.datetime.min
        
        self.who_booked = who_booked if who_booked is not None else [""]
        self.who_played = who_played


    def __str__(self):
        if len(self.who_booked) == 0:
            booked = "No one yet booked this session"
        else:
            booked = ", ".join(player.name for player in self.who_booked)

        played = ", ".join(player.name for player in self.who_played)

        to_string = "" 
        to_string += f"Date: {self.date}\n"
        to_string += f"Booked by: {booked}\n"
        to_string += f"Players: {played}"

        return to_string
    
    