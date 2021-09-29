# Author MB 09/28/2021

team1 = int(input("how many wins did team 1 have"))
team1_2 = int(input("how many ties did team 1 have"))

team2 = int(input("how many wins did team 2 have"))
team2_2 = int(input("how many ties did team 2 have"))

total_team1 = (3 * team1) + team1_2
total_team2 = (3 * team2) + team2_2

total_team1 = str(total_team1)
total_team2 = str(total_team2)

print("team one got" + " " + total_team1 + " " "points")
print("team two got" + " " + total_team2 + " " + "points")
