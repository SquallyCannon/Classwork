'''This code shows items a player can obtain on each level in a game.
Notice that the rock is not attainable on level 2.

Hey wait.
'''


'''HEY!'''
items = ['Wand', 'Rock', 'Pogo Stick']
levels = [1, 2, 3]
for level in levels:
    for item in items:
        if level == 2 and item == 'Rock':
            continue
        else:
            print(f"You can get a {item} at level {level}.")
print(__doc__)