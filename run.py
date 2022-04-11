import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('scores.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python-quiz-sheet')

results = SHEET.worksheet('results')

data = results.get_all_records()

# Define variables where to put name and score from the game to sheet
row = results.row_values(1)
col = results.col_values(1)
cell = results.cell(1,2).value

print(cell)

# Welcome text and rules
print("-" * 35)
print("""WELCOME TO MY PYTHON-MADE QUIZ!
GOOD LUCK!""")
print("-" * 35)


start_game = input("Type (yes) to start the game! ")
if start_game != "yes":
    print("Goodbye!")
    quit()

score = 0
name = input("What should we call you? ")
print(f"Alright {name}, let's play!")


# The game starts here



# Add username & score to google sheet
def add_user_score():
    insertRow = [name, score]
    results.append_row(insertRow, table_range="A1")

addUser = input("Do you want to save your username and score to google sheets? (yes/no) ")
if addUser == "yes":
    add_user_score()

