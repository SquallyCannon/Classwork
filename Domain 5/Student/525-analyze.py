coins = 5
games = 2
try:
    result = coins/games
except:
    print('This did not work. Did you to divide by zero?')
else:
    print('You are averaging', coins/games, 'coins per game.')
finally:
    print('Thank you for playing')