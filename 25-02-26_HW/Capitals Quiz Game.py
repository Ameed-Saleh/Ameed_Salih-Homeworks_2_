# Homework – Capitals Quiz Game (Functions & Game Flow)

## Question – Build the Game Flow Using Functions
'''
<img src="guess_capital.png" />

You are given the following data:
## 🎯 Your Goal
Build a **capital quiz game** using functions.
The player must:
* Reach **5 correct answers** → WIN
* Or if they make **3 mistakes** → LOSE

## 📌 Rules
* Do NOT change the given data (questions and answers lists)
* Use functions properly (no duplicated logic)
* Keep your code clean and readable
* Import and use `random`

## 🚀 Bonus (Optional)
* Add input validation (only allow numbers 1–4)
* if the user was wrong, tell him what was the correct city (hint: use split)
'''
questions = [
    "What is the capital of France? (1) Paris (2) Lyon (3) Marseille (4) Nice",                     # 0
    "What is the capital of Italy? (1) Milan (2) Venice (3) Rome (4) Naples",                       # 1
    "What is the capital of Spain? (1) Barcelona (2) Seville (3) Madrid (4) Valencia",              # 2
    "What is the capital of Portugal? (1) Porto (2) Lisbon (3) Faro (4) Braga",                     # 3
    "What is the capital of Greece? (1) Thessaloniki (2) Athens (3) Patras (4) Heraklion",          # 4
    "What is the capital of Netherlands? (1) Rotterdam (2) Utrecht (3) Eindhoven (4) Amsterdam",    # 5
    "What is the capital of Belgium? (1) Antwerp (2) Bruges (3) Brussels (4) Ghent",                # 6
    "What is the capital of Switzerland? (1) Zurich (2) Geneva (3) Basel (4) Bern",                 # 7
    "What is the capital of Austria? (1) Salzburg (2) Vienna (3) Graz (4) Innsbruck",               # 8
    "What is the capital of Canada? (1) Toronto (2) Vancouver (3) Ottawa (4) Montreal",             # 9
    "What is the capital of Brazil? (1) Rio de Janeiro (2) São Paulo (3) Brasília (4) Salvador",    # 10
    "What is the capital of Japan? (1) Osaka (2) Tokyo (3) Kyoto (4) Hiroshima",                    # 11
    "What is the capital of Australia? (1) Sydney (2) Melbourne (3) Canberra (4) Perth",            # 12
    "What is the capital of India? (1) Mumbai (2) New Delhi (3) Bangalore (4) Chennai",             # 13
    "What is the capital of Egypt? (1) Alexandria (2) Giza (3) Cairo (4) Luxor",                    # 14
    "What is the capital of Mexico? (1) Guadalajara (2) Monterrey (3) Cancún (4) Mexico City",      # 15
    "What is the capital of Argentina? (1) Córdoba (2) Rosario (3) Mendoza (4) Buenos Aires",       # 16
    "What is the capital of South Korea? (1) Busan (2) Incheon (3) Seoul (4) Daegu",                # 17
    "What is the capital of Sweden? (1) Gothenburg (2) Malmö (3) Uppsala (4) Stockholm",            # 18
    "What is the capital of Norway? (1) Bergen (2) Oslo (3) Trondheim (4) Stavanger"                # 19
]

#          0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
answers = [1, 3, 3, 2, 2, 4, 3, 4, 2, 3, 3, 2, 3, 2, 3, 4, 4, 3, 4, 2]
import random
## 🧠 What You Should Implement
## You must create and implement the following functions:
SKY = "\033[1;34;40m"
GREEN = "\033[0;32;40m"
RED = "\033[0;31;40m"
YELLOW = "\033[1;33;40m"
WHITE = "\033[1;37;40m"
PINK = "\033[1;35;40m"
RESET = "\033[0m"

def get_random_question():
    '''Returns a random index from the questions list'''
    return random.randint(0, len(questions) - 1)

def display_question(index):
    '''Prints the question at the given index'''
    print(" ")
    print(f"{SKY}The Question: {RESET} {WHITE}{questions[index]}{RESET} ")

def get_user_choice():
    '''Returns a user choice as an integer'''
    while True:
        choice = input(F"{YELLOW}Which of the following is the correct answer[1-4]?: {RESET}")
        if choice.isdigit() and 1 <= int(choice) <= 4:
            return int(choice)
        print(f"{RED}Invalid input. Please enter a number between 1 and 4.{RESET}")


def  user_answer_is_correct(index, choice):
    '''
    Returns True if the answer is correct
    Returns False otherwise'''
    return answers[index] == choice

def remove_question(index):
    '''
    Removes the question at the given index'''
    questions.pop(index)
    answers.pop(index)

def check_if_score_is_5(user_score):
    '''
    Returns True if the score is 5'''
    return user_score == 5

def check_if_miss_is_3(user_miss):
    '''Returns True if miss == 3'''
    return user_miss == 3

## 🔄 Game Flow (Main Logic)
## Your program should follow this structure:
score = 0
miss = 0
print(F"{SKY}Welcome to the World Capitals Quiz!{RESET}")
print(F"{SKY}Rules: Get 5 right to win. 3 wrong and you're out.{RESET}")
print("-" * 50)
while True:
    question_index = get_random_question()
    display_question(question_index)
    user_choice = get_user_choice()
    if  user_answer_is_correct(question_index, user_choice) :
        score += 1
        print(f'{GREEN}✅ You are correct{RESET}')
    else:
        miss += 1
        print(f'{RED}❌ You are wrong!{RESET}')
        print(f"{GREEN}the correct answer was {answers[question_index]}{RESET}")
    # remove the used question so it will not appear again
    remove_question(question_index)
    print(f"{GREEN}Score: {score} |{RED} Miss: {miss}{RESET}")
    if check_if_score_is_5(score):
        print(f'{PINK}WINNER 🏆!!!{RESET}')
        break

    if check_if_miss_is_3(miss):
        print(F'{PINK}YOU LOST 💀!!!{RESET}')
        break