'''
שאלה 2 – מערכת הצבעות ובדיקת מצביעים כפולים
קלוט מהמשתמש מספר ת.ז. של מצביע (נניח שמדובר במספרים בין 1 ל־100)

כללים:

כל מצביע שנקלט – הכנס לרשימה בשם votes
קולטים רק את ת.ז. של המצביע, ולא את ההצבעה עצמה
ייתכן שאותו מצביע ינסה להצביע יותר מפעם אחת
הקלט מסתיים כאשר מתקבל הערך 999-
לאחר סיום הקלט:

צור set של מצביעים ייחודיים מתוך הרשימה

צור set נוסף בשם invalid_voters

עבור על כל המצביעים:

כל מצביע שהופיע יותר מפעם אחת – הסר אותו מקבוצת המצביעים החוקיים
הוסף אותו ל־invalid_voters
לבסוף הדפס:

את כל המצביעים החוקיים
את כל המצביעים הפסולים
כמה ניסיונות הצבעה היו היום (כלומר אורך הרשימה כולל כפילויות)
רמזים:

ניתן להשתמש ב־count
ניתן לעבור על set כדי לא לחזור על אותו מצביע שוב ושוב
Example (דוגמה למערך + פלט)
נניח שבסוף היום הרשימה יצאה ככה (כולל כפילויות):

votes = [10, 7, 10, 3, 3, 50, 99]
ספירה:

10 הופיע פעמיים ⇒ פסול
3 הופיע פעמיים ⇒ פסול
7, 50, 99 הופיעו פעם אחת ⇒ חוקיים
פלט צפוי:

מצביעים חוקיים: [7, 50, 99]
מצביעים פסולים: [3, 10]
מספר ניסיונות הצבעה היום: 7
'''

votes = []
while True:
    input_id = input("enter your id number that be between 1-100,[-999 to end] -->")
    if input_id == '-999':
        break
    if not input_id.isdigit():
        print("invalid , enter digits only no alpha !!")
        continue
    voter_id = int(input_id)  
    if 1<= voter_id <=100: 
        votes.append(voter_id)
    else:
        print("id not in range!!!!")
print(f"votes = {votes}")     
  
unique_voters = set(votes)
invalid_voters = set()
valid_voters = unique_voters.copy()
for voter in unique_voters:
    if votes.count(voter) > 1:
        valid_voters.remove(voter)
        invalid_voters.add(voter)
    print(voter ,"voted" ,votes.count(voter),"times")

print(f"valid voters --> {valid_voters}")
print(f"invalid voters --> {invalid_voters}")
print(f"number of votes is --> {len(votes)}")

