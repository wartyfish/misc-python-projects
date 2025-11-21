import datetime

class Participant:
    def __init__(self, name: str):
        self.name = name
        self.times_played = 0
        self.times_booked = 0
        self.sessions_booked = []
        self.sessions_played = []        
        self.due_to_book = ""

    @property
    def bookings_per_session(self):
        if self.times_played == 0:
            return 0
        else:
            return self.times_booked / self.times_played
        
    @property
    def most_recent_booking(self):
        if len(self.sessions_booked) > 0:
            return sorted(
                self.sessions_booked,
                reverse=True
            )[0]
        else:
            return datetime.datetime.min
        
    @property
    def sessions_since_last_booking(self):
        result = 0
        for date in sorted(
            self.sessions_played,
            reverse=True
        ):
            if date == self.most_recent_booking:
                break
            else:
                result += 1 

        return result

    
    def __str__(self):
        to_string = f"{self.name:6} "
        to_string += f"Sessions played: {self.times_played:2}, "
        to_string += f"Sessions booked: {self.times_booked:2}, "
        to_string += f"Sessions since last booking: {self.sessions_since_last_booking:2}, "
        to_string += f"Due to book? {self.due_to_book}"

        return to_string
    
    # record booking
    def booked(self, date):
        self.times_booked += 1
        #self.time_since = 0
        self.sessions_booked.append(date)

    # record session played
    def played(self, date):
        self.times_played += 1
        #if self.time_since == -1:
        #    self.time_since = 0
        #self.time_since += 1
        self.sessions_played.append(date)