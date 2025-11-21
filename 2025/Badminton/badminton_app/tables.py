def print_log(session_manager):
    print(f"Date{" "*4}|Booked{" "*9}|Played")

    for s in session_manager.sessions_sorted:
        who_booked = ", ".join(sorted(player.name for player in s.who_booked))
        who_played = ", ".join(sorted(player.name for player in s.who_played))

        print(f"{s.date}|{who_booked:15}|{who_played}")

    print()

def print_processed(player_registry):
    rows = []

    for player in sorted(
        player_registry.all(), 
        key=lambda p: (-1* p.sessions_since_last_booking, p.bookings_per_session, p.most_recent_booking)
    ):
        rows.append([
            player.name,
            player.times_played,
            player.times_booked,
            player.sessions_since_last_booking,
            round(player.bookings_per_session, 2),
            player.due_to_book
        ])

    print(f"{" "*10}|{"Sessions".center(15)}|{"Sessions".center(15)}|{"Sessions since".center(15)}|{"Bookings per".center(15)}|{"Due to".center(10)}")
    print(f"{"Name".center(10)}|{"played".center(15)}|{"booked ".center(15)}|{"last booking".center(15)}|{"session".center(15)}|{"book?".center(10)}")

    for row in rows:
        print(f"{row[0]:9} |",end="")
        print(f"{row[1]:14} |",end="")
        print(f"{row[2]:14} |",end="")
        print(f"{row[3]:14} |",end="")
        print(f"{row[4]:14} |",end="")
        print(f"{row[5]:>9}")        

    print()