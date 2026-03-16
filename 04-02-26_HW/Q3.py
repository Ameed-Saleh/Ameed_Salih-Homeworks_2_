'''
Question 3 – Restaurant recommendation (booleans)
Input from the user

The time it took the restaurant to bring the meal (in minutes)
The price of the meal (in shekels)
Create boolean variables

is_quick_service – True if the time is less than 15 minutes, otherwise False
is_expensive – True if the price is more than 100 shekels, otherwise False
Now check

If is_quick_service and not is_expensive print recommended
Otherwise print not recommended
'''


import time
minutes: int = int(input("How long will it take to deliver the meal? "))
is_quick_service: bool = minutes <= 15
if not is_quick_service:
    time.sleep(1)
    print("--- It's been too long than I thought ")
else:
    print("--- Okay, you can start preparing the meal ")

print("-"*40)
shekels:int = int(input("What is the price of the meal?"))
is_expensive: bool = shekels > 100
if is_expensive:
    print("--- The price of this meal is expensive!!")
else:
    time.sleep(1)
    print("--- The price of this meal is not expensive at all")

print("*"*40)
time.sleep(2)
if is_quick_service and not is_expensive:
    print("--- Highly recommended")
else:
    print ("--- not recommended ")