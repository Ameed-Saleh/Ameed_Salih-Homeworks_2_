'''
שאלה 2 – גיבוי וניקוי רשימה
נתונה הרשימה:
grades = [85, 90, 78, 92, 88]
בצע את הפעולות הבאות:

1- צור עותק גיבוי של הרשימה
2- נקה את הרשימה המקורית
3- הדפס את שתי הרשימות כדי להוכיח שהעותק נשמר
4- חבר את הרשימה [100, 95] לרשימת הגיבוי בשתי דרכים שונות :

פעם אחת עם +
פעם אחת עם extend
יש להשתמש ב: copy, clear, extend
'''

grades = [85, 90, 78, 92, 88]
backup = grades.copy()
grades.clear()
print(f"grades after clear = {grades}")
print(f"backup after copy grades = {backup}")

new_list = [95, 100]
backup += new_list
print(f"backup + new_list = {backup}")

backup.extend(new_list)
print(f"backup with extend = {backup}")