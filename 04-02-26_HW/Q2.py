'''
Question 2 – Countdown with time.sleep
Use the time.sleep function to create the following output

Print 5
[Sleep 1 second]
Print 4
[Sleep 1 second]
Print 3
[Sleep 1 second]
Print 2
[Sleep 1 second]
Print 1
[Sleep 1 second]
Print 0 - Launch 🚀
Rules

Use import time
Use time.sleep(1) between prints
'''

print ("question", 2)
import time
i = 5
while i >0:
    time.sleep(1)
    print (i)
    i -= 1
else:
    print(0, '- launch🚀')