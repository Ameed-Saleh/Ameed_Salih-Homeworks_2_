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

while True:
    _rating = int(input("Enter a number between 1 and 5: "))
    _valid = 1 <= _rating <= 5
    if _valid:
        print("valid")
    else:
        print("invalid")
    _best = _rating == 5
    if _best:
        print("best")
    else:
        print("not best")
    _medium = 2 < _rating < 4
    if _valid and not _medium:
        print("score high or low")
    else:
        print("medium")

    _num = int(input("Enter a number: "))
    _positive = _num >= 0
    if _positive:
        print("positive")
    else:
        print("negative")
    _even = _num % 2 == 0
    if _even:
        print("even")
    else:
        print("odd")