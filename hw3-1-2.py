# Author MB 09/29/2021

card1 = int(input("how much is card 1"))
card2 = int(input("how much is card 2"))

total_card = card1 + card2

if total_card > 21:
    print("you bust")

if total_card < 21:
    print("you are safe")
