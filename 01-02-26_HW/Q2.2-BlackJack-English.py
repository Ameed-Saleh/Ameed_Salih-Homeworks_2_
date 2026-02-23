import random
GREEN = "\033[0;32m"
BLUE= "\033[1;34;40m"
RED = "\033[1;31;40m"
RESET = "\033[0m"
suits = ["❤️", "♦️", "♣️", "♠️"]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q" , "K", "A"]
p_1 = 0
print(f"{GREEN} player 1 start {RESET}")
p1_cards =" "

for i in [1 , 2]:
    suit = random.choice(suits)
    card = random.choice(cards)
    p1_cards += suit + str(card)+ " "
    if card== "J" or card == "Q" or card == "K":
        p_1 += 10
    elif card == "A":
        p_1 += 1
    else:
        p_1 += card
while True:
    print(f"{RED} player 1 cards = {RESET}", p1_cards)
    print(f"{BLUE} total cards =  {RESET}",p_1)
    if p_1 >= 21:
        if p_1 > 21:
            print("you loose!")
        print("-" * 30)
        break
    else:
        choice = input("|continue✅=1| or |stop❌=0|:")
        if choice == "1":
            suit = random.choice(suits)
            card = random.choice(cards)
            p1_cards += suit + str(card) + " "
            if card == "J" or card == "Q" or card == "K":
                p_1 += 10
            elif card == "A":
                p_1 += 1
            else:
                p_1 += card
        else:
            break
print(" ")
p_2 = 0
print(f"{GREEN} player 2 start {RESET}")
p2_cards =""
for i in [1 , 2]:
    suit = random.choice(suits)
    card = random.choice(cards)
    p2_cards += suit + str(card)+ " "
    if card== "J" or card == "Q" or card == "K":
        p_2 += 10
    elif card == "A":
        p_2 += 1
    else:
        p_2 += card
while True:
    print(f"{RED} player 2 cards = {RESET}", p2_cards)
    print(f"{BLUE} total cards =  {RESET}", p_2)
    if p_2 >= 21:
        if p_2 > 21:
            print("you loose!")
        print("-" * 30)
        break
    else:
        choice = input("|continue✅=1| or |stop❌=0|:")
        if choice == "1":
            suit = random.choice(suits)
            card = random.choice(cards)
            p2_cards += suit + str(card) + " "
            if card == "J" or card == "Q" or card == "K":
                p_2 += 10
            elif card == "A":
                p_2 -= 1
            else:
                p_2 += card
        else:
            break
print(" ")
print(f" {GREEN} ------------------  results  ------------------ {RESET}")
print(f"{RED} player 1 cards = {RESET}", p1_cards , f"{BLUE} total cards =  {RESET}", p_1)
print(f"{RED} player 2 cards = {RESET}", p2_cards ,f"{BLUE} total cards =  {RESET}", p_2)
if p_1 > 21 and p_2 > 21:
    print("both of you loose‼️💤!")
elif p_1 > 21 :
    print("player 1 loose, but the winner is player 2🥈!")
elif p_2 > 21:
    print("player 2 loose, but the winner is player 1🥇!")
elif p_1 > p_2:
    print("player 1 is the winner🥇!")
elif p_2 > p_1:
    print("player 2 is the winner🥈!")
else:
    print("--🫂TEKOOOOO --")
