coins = ('Bronze','Silver','Platinum','Gold')
scepter = False
for coin in coins:

    if coin == 'Platinum' and scepter:
        print('Congratulations! The platinum coin will move you to the next level!')
        continue
    print ('You possess a', coin, 'coin.')