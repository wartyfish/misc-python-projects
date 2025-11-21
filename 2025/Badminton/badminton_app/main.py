import sheets
import tables
from session_manager import SessionManager
from players import PlayerRegistry
import input_hanlders

def main():
    registry = PlayerRegistry()
    session_manager = SessionManager(registry)

    print("Fetching data from Google Sheets... ",end="")

    log, processed = sheets.load_sheets()
    sheets.read_sessions_from_sheets(log, session_manager)
    print("Success.\n")

    session_manager.update_all_stats()

    tables.print_log(session_manager)
    tables.print_processed(registry)

    while True:
        cmd = input ("0=exit, 1=update sheets, 2=add new session\n")
        if cmd == "0":
            break
        if cmd == "1":
            sheets.update_log_sheet(log, session_manager)
            sheets.update_processed_sheet(processed, registry)
        if cmd == "2":
            input_hanlders.input_new_session(registry, session_manager)

        
    

if __name__ == "__main__":
    main()