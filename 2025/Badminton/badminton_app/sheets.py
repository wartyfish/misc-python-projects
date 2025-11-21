import gspread
from google.oauth2.service_account import Credentials

def load_sheets():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(r"C:\Users\Eem\Documents\API_credentials\badminton_credentials.json", scopes=scopes)
    client = gspread.authorize(creds)

    book = client.open("Badminton Session Log")

    return book.worksheet("Log"), book.worksheet("Processed")

def read_sessions_from_sheets(sheet, session_manager):
    data = sheet.get_all_values()[1:] # skip header
    rows = [value[0:3] for value in data]
    rows = [row for row in rows if any(cell.strip() for cell in row)]

    for date, booked_str, played_str in rows:
        played = played_str.split(", ") if played_str else []
        booked = booked_str.split(", ") if booked_str else []
    
        session_manager.new_session(date, played, booked)

def update_log_sheet(sheet, session_manager):
    sheet.batch_clear(["A2:C1000"])

    rows = []
    for s in session_manager.sessions_sorted:
        rows.append([
            s.date,
            ", ".join(sorted([p.name for p in s.who_booked])),
            ", ".join(sorted([p.name for p in s.who_played]))
        ])
    
    if session_manager.is_most_recent_session_booked:
        sheet.update("A3", rows)
    else:
        sheet.update("A2", rows)
    
    print("Log updated successfully")

def update_processed_sheet(sheet, player_registry):
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
    
    print("Processed updated successfully")
    
    sheet.batch_clear(["A2:F"])   
    sheet.update(values=rows, range_name="A2")
    
