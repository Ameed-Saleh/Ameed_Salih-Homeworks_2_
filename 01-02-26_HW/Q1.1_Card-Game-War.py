import random
_round: int = 0
p_score: int = 0
c_score: int = 0
suits = ["❤️", "♦️", "♣️", "♠️"]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
print("--- ברוכים הבאים למשחק מלחמה! הראשון שמגיע ל-10 נקודות מנצח. ---")
while True:
    _round += 1
    _ = input("לסיבוב הבא תלחץ ENTER ")
    print()
    print(">>>>>>>>>> סיבוב ", _round, "<<<<<<<<<<")
    p_suit = random.choice(suits)
    p_card = random.choice(cards)
    c_suit = random.choice(suits)
    c_card= random.choice(cards)
    print("  הקלף שלך:", p_card, p_suit)
    print("  הקלף של המחשב:", c_card , c_suit)
    # מציאת הכוח של הקלף לפי המיקום שלו ברשימה
    p_val = cards.index(p_card)
    c_val = cards.index(c_card)
    if p_val > c_val:
        p_score += 1
        print("  >> ניצחת בסיבוב! 🎉")
    elif c_val > p_val:
        c_score += 1
        print("  >> המחשב ניצח בסיבוב... 🤖")
    else:
        print("  >> תיקו! אין נקודות.")
    print("  ניקוד נוכחי - אתה:", p_score, "| מחשב:", c_score)
    print("-" * 32)
    if p_score == 10:
       print("כל הכבוד! הגעת ל-10 נקודות וניצחת במשחק! 🏆")
       break
    elif c_score == 10:
        print("המשחק נגמר. המחשב הגיע ל-10 נקודות. אולי פעם הבאה! 💤")
        break

