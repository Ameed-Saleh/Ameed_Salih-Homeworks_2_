import random
_round: int = 0
p_score: int = 0
c_score: int = 0
J: int = 11
Q: int = 12
K: int = 13
A: int = 14
print("--- ברוכים הבאים למשחק מלחמה! הראשון שמגיע ל-10 נקודות מנצח. ---")
while True:
    _round += 1
    _ = input("לסיבוב הבא תלחץ ENTER ")
    print()
    print(">>>>>>> סיבוב: ", _round, "<<<<<<<")
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    player = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A])
    if player == J:
        print("Your card is ", "J", suit)
    elif player == Q:
        print("Your card is ", "Q", suit)
    elif player == K:
        print("Your card is ", "K", suit)
    elif player == A:
        print("Your card is ", "A", suit)
    else:
        print("Your card is ", player,  suit)
    c_suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    computer = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A])
    if computer == J:
        print("Computer's card is ", "J", suit)
    elif computer == Q:
        print("Computer's card is ", "Q", suit)
    elif computer == K:
        print("Computer's card is ", "K", suit)
    elif computer == A:
        print("Computer's card is ", "A", suit)
    else:
        print("Computer's card is ", computer, suit)
    if player > computer:
        print("  >> ניצחת בסיבוב! 🎉")
        p_score += 1
    elif player == computer:
        print("  >> תיקו! אין נקודות.")
    else:
        print("  >> המחשב ניצח בסיבוב... 🤖")
        c_score += 1
    print("  ניקוד נוכחי - אתה:", p_score, "| מחשב:", c_score)
    print("-" * 32)
    if p_score == 10:
       print("\nכל הכבוד! הגעת ל-10 נקודות וניצחת במשחק! 🏆")
       break
    elif c_score == 10:
        print("המשחק נגמר. המחשב הגיע ל-10 נקודות. אולי פעם הבאה! 💤")
        break