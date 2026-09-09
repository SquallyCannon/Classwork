coins = ['Bronze', 'Silver', 'Gold','Platinum']
coin = 'gold'
score = 10000

if score > 10000:
    if coin in ('Gold','Platinum'):
        print("You have reached level 3") #expected
    else:
        print("You have reached level 2")
elif score > 5000 and coin in coins:
    print("You have reached level 1. Keep going")
else:
    print("Increase your score and collect coins to move up")