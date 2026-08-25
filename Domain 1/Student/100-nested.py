game_state = True
game_lives = 1
while game_lives < 3:
    for i in range(10):
        print("You have reached position", i, "in game life", game_lives)
    if game_state == True:
        game_lives +=1
print(f"Thank you for playing. {game_lives}")
