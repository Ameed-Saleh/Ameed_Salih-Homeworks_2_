'''
Question 1 – Print numbers in range (no return)
Write a function that gets two int parameters: start and stop
The function should print all numbers from start to stop (inclusive)
Notes:
This function does not return a value
Use a loop (for with range) inside the function
Demo (example usage)
print_numbers(3, 7)
# expected output:
# 3
# 4
# 5
# 6
# 7
'''

num1 = int(input("Enter start number: "))
num2 = int(input("Enter stop number: "))
def print_numbers(_start:int, _stop:int):
    for i in range(_start, _stop+1):
        print(i)
print_numbers(num1, num2)