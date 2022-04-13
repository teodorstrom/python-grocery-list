import gspread
from google.oauth2.service_account import Credentials

# create a client to interact with the Google Drive API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python-quiz-sheet')

results = SHEET.worksheet('results')
data = results.get_all_records()

# Welcome text, rules and let's the user input their name
print("-" * 35)
print("""WELCOME TO MY PYTHON-MADE QUIZ!
GOOD LUCK!
OBS - This game is NOT case sensetive
YoUr anSWers CaN be LIke thIs
""")
print("-" * 35)
score = 0
name = input("What should we call you? ")


"""End game function will be called inside
the play_game function.
"""
def end_game():
    print("-" * 35)
    print("GAME OVER")
    print("-" * 35)
    print(name + ",", "your total score was:", score)


"""
The game as a function.
Simply 5 questions that will response with different print statements
regarding how the player will answer.
Score value will increase with 1 if correct answer is given.
"""
def play_game():
    global score

    # Questions
    question1 = input("What does HTML stand for? ")
    if question1.lower() == "hypertext markup language":
        print("Correct!")
        score += 1
        print(f"Your score is {score}")
        print("-" * 35)
    else:
        print("Incorrect! Correct answer is: HyperText Markup Language")
        print(f"Your score is {score}")
        print("-" * 35)

    question2 = input("What does CSS stand for? ")
    if question2.lower() == "cascading style sheets":
        print("Correct!")
        score += 1
        print(f"Your score is {score}")
        print("-" * 35)
    else:
        print("Incorrect! Correct answer is: Cascading Style Sheets")
        print(f"Your score is {score}")
        print("-" * 35)

    question3 = input("What does JS stand for? ")
    if question3.lower() == "javascript":
        print("Correct!")
        score += 1
        print(f"Your score is {score}")
        print("-" * 35)
    else:
        print("Incorrect! Correct answer is: JavaScript")
        print(f"Your score is {score}")
        print("-" * 35)

    question4 = input("Python was released puplicly in year: ")
    if question4.lower() == "1991":
        print("Correct!")
        score += 1
        print(f"Your score is {score}")
        print("-" * 35)
    else:
        print("Incorrect! Correct answer is: 1991")
        print(f"Your score is {score}")
        print("-" * 35)

    question5 = input("Python was created by ")
    if question5.lower() == "guido van rossum":
        print("Correct!")
        score += 1
        print(f"Your score is {score}")
    else:
        print("Incorrect! Correct answer is: Guido Van Rossum")
        print(f"Your score is {score}")

    end_game()


# The game starts here
start_game = input(f"Alright {name}, type (yes) to start the game: ")
print("-" * 35)
if start_game == "yes":
    play_game()
else:
    print("Goodbye!")
    quit()


"""The player will be asked if they want to save their name and score to a 
google sheets document. The data will always be printed in the bottom of the 
list in the document.
"""
def add_user_score():
    insertRow = [name, score]
    results.append_row(insertRow, table_range="A1")

print("Do you want to save your name and score to google sheets?")
addUser = input("yes/no: ")
if addUser == "yes":
    add_user_score()
    print("Results has been successfully added to the google sheet, goodbye!")
    quit()
else:
    print("Okey, thank you for playing! :)")
    quit()

