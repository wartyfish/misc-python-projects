# Badminton Session Tracker

A python application for keeping track of badminton sessions played with my friends. It tracks player participation and booking history using Google Sheets, and can determine who is due to book the next session.

## Features
- Reads session data from Google Sheets
- Determines who is due to book
- Tracks player participation statistics
- Command-line interface for adding sessions

## Project structure
main.py               # Entry point / CLI

sheets.py             # Google Shets read/write operations

session_manager.py    # Session creation and update player stats

players.py            # Player registry and lookups

print_views.py        # Console output formatting

input_handlers.py     # CLI input handling


models/
participant.py        # Participant model
session.py            # Session model
