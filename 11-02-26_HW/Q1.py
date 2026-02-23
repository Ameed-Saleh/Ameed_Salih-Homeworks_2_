'''
שאלה 1 – פעולות בסיסיות על רשימה
נתונה הרשימה:

numbers = [10, 20, 30, 20, 40, 50]
בצע את הפעולות הבאות:

הדפס כמה פעמים המספר 20 מופיע ברשימה
הדפס את האינדקס של ההופעה הראשונה של 30
הוסף את המספר 99 לסוף הרשימה
הכנס את המספר 15 לאינדקס 2
מחק את ההופעה הראשונה של 20
הסר את הערך שנמצא באינדקס 3 באמצעות pop והדפס מה הוסר
הדפס את הערך המקסימלי ברשימה
הדפס את הערך המינימלי ברשימה
הדפס את סכום כל האיברים
הדפס את הממוצע בעזרת statistics.mean
הדפס כמה איברים יש ברשימה
יש להשתמש ב: count, index, append, insert, remove, pop, max, min, sum, len
'''

numbers = [10, 20, 30, 20, 40, 50]
print(f"numbers list is: {numbers}")
print(f"number 20 appears ,{numbers.count(20)} times.")

print("the first 30 index is",numbers.index(30))

numbers.append(99)
print(f"append number 99 to numbers: {numbers}")

numbers.insert(2,15)
print(f"insert 15 at index 2 to numbers : {numbers}")

numbers.remove(20)
print(f"remove the first 20 from numbers : {numbers}")

print(f"number removed: {numbers.pop(3)}")

print(f"maximum number is: {max(numbers)}")
print(f"minimum number is: {min(numbers)}")
print(f"total sum numbers: {sum(numbers)}")

import statistics
print(f"average numbers: {statistics.mean(numbers):.2f}")

print(f"the length of numbers: {len(numbers)}")
print("*" * 30)
print(f"The New List Of Numbers Is: {numbers}")
