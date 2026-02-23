import random
suits = ["❤️", "♦️", "♣️", "♠️"]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
print("----- תור שחקן 1 -----")
player_1 = 0
p1_cards =""
for i in [1 , 2]:
    suit_1 = random.choice(suits)
    card = random.choice(cards)
    p1_cards = p1_cards + str(card) + suit_1 + " "
    if card== "A":
        player_1 += 1
    elif card== "J" or card == "Q" or card == "K":
        player_1 += 10
    else:
        player_1 += card
while True:
    print("הקלפים שלך: " , p1_cards)
    print("סכום: " , str(player_1))
    if player_1 >= 21:
        if player_1 > 21: print("נפסלת!")
        print("-" * 30)
        break
    else:
        choice = input("CONTINUE✅ = 1 |or| STOP❌ = 0 ")
        if choice == "1":
            card = random.choice(cards)
            suit = random.choice(suits)
            p1_cards = p1_cards + str(card) + suit + " "
            if card == "A":
                player_1 = player_1 + 1
            elif card == "J" or card == "Q" or card == "K":
                player_1 = player_1 + 10
            else:
                player_1 = player_1 + card
        else:
            break
print(" ")
print("----- תור שחקן2  -----")
player_2 = 0
p2_cards = ""
for i in [1 , 2]:
    suit_2 = random.choice(suits)
    card = random.choice(cards)
    p2_cards = p2_cards + str(card) + suit_2 + " "
    if card== "A":
        player_2 += 1
    elif card== "J" or card == "Q" or card == "K":
        player_2 += 10
    else:
        player_2 += card
while True:
    print("הקלפים שלך: " + p2_cards)
    print("סכום: " + str(player_2))
    if player_2 >= 21:
        if player_2 > 21:  print("נפסלת!")
        print("-" * 20)
        break
    else:
        choice = input("CONTINUE✅ = 1 |or| STOP❌ = 0 ")
        if choice == "1":
            card = random.choice(cards)
            p2_suit = random.choice(suits)
            p2_cards = p2_cards + str(card) + p2_suit + " "
            if card == "A":
                player_2 = player_2 + 1
            elif card == "J" or card == "Q" or card == "K":
                player_2 = player_2 + 10
            else:
                player_2 = player_2 + card
        else:
            break
print(" ")
print("תוצאות סופיות 🟰")
print("הקלפים של שחקן 1: " , p1_cards , "סכומם: " , player_1)
print("הקלפים של שחקן 2: " , p2_cards , "סכומם: " , player_2)
if player_1 > 21 and player_2 > 21:
    print("שניכם נפסלתם‼️💤")
elif player_1 > 21:
    print("שחקן 2 מנצח במשחק! 🥈")
elif player_2 > 21:
    print("שחקן 1 מנצח במשחק! 🥇")
elif player_1 > player_2:
    print("שחקן 1 מנצח במשחק! 🥇")
elif player_2 > player_1:
    print("שחקן 2 מנצח במשחק! 🥈")
else:
    print("תיקו!🫂🤝🏼")