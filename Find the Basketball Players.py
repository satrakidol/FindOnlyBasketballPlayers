football_players = {"Eve", "Tom", "Richard", "Peter"}
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}

Only_basketball_players=[]

for player in basketball_players:
    if player not in volleyball_players and player not in football_players:
        Only_basketball_players.append(player)

print(Only_basketball_players)
