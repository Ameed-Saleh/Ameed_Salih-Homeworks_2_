'''
Question 2 – Basic math list (returns a list)
Write a function that gets two numbers a and b and returns a list in this exact order:
[a+b, a-b, a/b, a*b]

Notes:

The function returns the list
Assume b != 0 (no need to handle division by zero)
Demo (example usage)
result = basic_math_list(10, 2)
print(result)
# expected output:
# [12, 8, 5.0, 20]
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
def basic_math_list(a: int, b: int) -> list:
    return [a + b, a - b, a * b, a / b]
print(basic_math_list(num1, num2))



