'''
✨✨ Question 3 – Bonus challenge: Mini math game -- Experts only! ✨✨

Implement a small game

The computer should:

Pick a random number between 1 and 10
Pick a random operation from: +, -, *, %
Pick another random number between 1 and 10
Print the equation and ask the user for the result
Rules:

If the user is correct, print Correct!
Otherwise print Wrong.. the answer was ___
Your task
You will get the main code below

Your job is to complete the missing functions:

get_random_between_1_10()
get_random_operation()
calc_result(num1, oper, num2)
Main code (DO NOT CHANGE)
num1 = get_random_between_1_10()
oper = get_random_operation()
num2 = get_random_between_1_10()
result = calc_result(num1, oper, num2)

print(f"{num1} {oper} {num2} = ?")
user_result = int(input('whats the result? '))

if result == user_result:
    print('Correct!')
else:
    print(f"Wrong.. the answer was {result}")
Starter code (complete the TODOs)
import random

def get_random_between_1_10() -> int:
    """Return a random integer between 1 and 10 (inclusive)."""
    # TODO: implement
    pass
def get_random_operation() -> str:
    """Return a random operation symbol: one of '+', '-', '*', '%'"""
    # TODO: implement
    pass


def calc_result(num1: int, oper: str, num2: int) -> int:
    """Calculate and return the result of: num1 oper num2

    Supported operations: +, -, *, %

    Example:
        calc_result(7, '*', 3) -> 21
    """
    # TODO: implement
    pass
Demo (example run)
Example 1:

8 * 4 = ?
whats the result? 32
Correct!
Example 2:

9 % 2 = ?
whats the result? 3
Wrong.. the answer was 1
'''

import random
from unittest import case

SKY = "\033[1;34;40m"
GREEN = "\033[0;32;40m"
RED = "\033[0;31;40m"
RESET = "\033[0m"

def get_random_between_1_10() -> int:
    return random.randint(1, 10)

def get_random_operation() -> str:
    return random.choice(['+', '-', '*', '%', '//'])

def calc_result(num1: int, oper: str, num2: int) -> int:
    match oper:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '%':
            return num1 % num2
        case '//':
            return num1 // num2
current_round = 0
max_rounds = 10
while True:
    current_round += 1
    num1 = get_random_between_1_10()
    oper = get_random_operation()
    num2 = get_random_between_1_10()
    result = calc_result(num1, oper, num2)
    print(f"{SKY}       round {current_round}      {RESET}")
    print(f"{num1} {oper} {num2} = ?")
    user_result = int(input('whats the result? '))
    if current_round == max_rounds:
        break
    if result == user_result:
        print(f"{GREEN}Correct answer!{RESET}")
        print("")
    else:
        print(f"{RED} Wrong.... the answer was {result} {RESET}")
        print("-" * 30)






