'''This file is used for game were you do noting and lose. 
Tells players what positions they have reached in each stage in a game.'''


game_state = True
game_lives = 1
while game_lives <= 3:
    for i in range(1,11):
        print("You have reached position", i, "in game life", game_lives)
    if game_state == True:
        game_lives +=1
print("Thank you for playing.")

print(__doc__)