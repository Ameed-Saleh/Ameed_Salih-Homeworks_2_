'''
Question 1 – Sound system (match-case)
In a sound system there are volume levels from 1–10

1 – very quiet
2 – quiet
3 – low
4 – low
5 – medium
6 – medium high
7 – loud
8 – very loud
9 and 10 – max volume
Tasks

Input an integer from the user (1–10)
Use match case to display the correct sound description
If the number is not between 1–10 print invalid volume
'''

print("question", 1)
while True:
   volume:int = int(input("Enter a volume level to check a sound system:"))
   print(volume , end=" - ")
   match volume:
       case 1:
           print("Very Quit")
       case 2 :
           print("Quit")
       case 3 | 4 :
           print("Low")
       case 5 :
           print("Medium")
       case 6 :
           print("Medium High")
       case 7 :
           print ("Loud")
       case 8 :
         print("Very Loud")
       case 9 | 10 :
           print("Max Volume")
       case _ :
           print("invalid volume")