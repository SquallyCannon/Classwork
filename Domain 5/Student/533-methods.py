import random
class Game_Player:
    def __init__(character,name, base_score=0, rank=1):
        character.name = name
        character.score = base_score
        character.rank = rank
    def get_score(character, interval=10):
        character.score += interval * character.rank
        return character.score
    
game_player1 = Game_Player("HELLO",0,10)
game_player2 = Game_Player("HI",1000)
game_player3 = Game_Player("HEY",5,2)
game_player4 = Game_Player("SUP",100,3)
game_player5 = Game_Player("GREETINGS",1000,1)

players = [game_player1,game_player2,game_player3,game_player4,game_player5]
for player in players:
     player.get_score(random.randint(0,1000))
best = players[0]
for player in players:
    if player.score > best.score:
        best = player
print(best.name, best.score)
