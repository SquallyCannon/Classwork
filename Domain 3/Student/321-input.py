named = False
while named == False:
    player_name = input("Please enter your first name: ")
    if len(player_name) < 3:
        print("Names must be atleast three charactors")
    else:
        named = True
print("Welcome to the game,",player_name)