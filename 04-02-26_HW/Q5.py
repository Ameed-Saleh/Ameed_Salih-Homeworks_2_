'''
Question 5 – Password Validation
'''

import random
print("_" * 45)
password: str = random.choice(["@A24sal01", "aSal$A", "2401sa", "A24SaL1"])
print(f"password: {password} your password is in length: {len(password)}")
print("*" * 20)
upper =0
lower = 0
digit = 0
i = 0
while i < len(password):
    x = password[i]
    if x.isalpha():
        if x.isupper():
            print (x , "is uppercase")
            upper += 1
        elif x.lower():
            print (x , "is lowercase")
            lower += 1
    elif x.isdigit() :
        print(x ,"is digit")
        digit += 1
    i += 1
print("*" * 20)
if upper > 0 and lower > 0 and digit > 0:
    print("Valid Password")
else:
    print("Invalid Password")