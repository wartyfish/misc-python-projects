import gspread
from google.oauth2.service_account import Credentials

# Define the required API scopes (permissions)
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate using the service account credentials and scopes
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

# Open the spreadsheet by name
sheet = client.open("Badminton Session Log").sheet1

# Try reading the first few rows
rows = sheet.get_all_records()
print("Connected successfully! First few rows:")
print(rows[:3])
