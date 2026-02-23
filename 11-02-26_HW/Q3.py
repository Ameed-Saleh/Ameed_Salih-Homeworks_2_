'''
⭐⭐ בונוס: ⭐⭐
רשות -- שאלה 3 – any ו-all (מחרוזות)
צור את הרשימה הבאה:
words = ["HELLO", "WORLD", "PYTHON", "CODE", "DEVELOPER", "AI"]
בצע את הבדיקות הבאות:

1- בדוק אם כל המילים כתובות באותיות גדולות בלבד
השתמש ב־all

2- בדוק אם קיימת לפחות מילה אחת עם יותר מ־5 תווים
השתמש ב־any
'''

words = ["HELLO", "WORLD", "PYTHON", "CODE", "DEVELOPER", "AI"]

print(all(word.isupper() for word in words))
print(not any(word.islower() for word in words))

print("*" * 5)

print(any(len(word)>5 for word in words))
