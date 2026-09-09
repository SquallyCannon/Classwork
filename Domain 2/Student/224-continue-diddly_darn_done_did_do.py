coins = ('Bronze','Silver','Platinum','Gold')
for coin in coins:
    if coin != 'Platinum':
        print ('You possess a', coin, 'coin.')
    elif coin == 'Platinum':
        print('Congratulations! The platinum coin will move you to the next level!')
        continue
    