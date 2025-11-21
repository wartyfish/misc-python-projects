import datetime
import tables

def input_new_session(registry, session_manager):
    while True:
        while True:
            date = input("Date (dd/mm/yy): ")
            try:
                datetime.datetime.strptime(date, "%d/%m/%y")
                break
            except:
                print("Date must be dd/mm/yy")
        
        played = input("Who played (comma seperated):\n").split(", ")
        booked_raw = input("Who booked (optional, comma seperated):\n").strip()
        booked = booked_raw.split(", ") if booked_raw else []

        cmd = input("Commit? [y/n] ").lower()
        if cmd == "y":
            new_session = session_manager.new_session(date, played, booked)
            session_manager.update_player_stats(new_session)
        
            tables.print_log(session_manager)
            tables.print_processed(registry)

            break
