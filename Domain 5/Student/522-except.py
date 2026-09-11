figuratives = ['Simile','Metaphor','Personification','Hyperbole','Allusion']
try:
    figurative_input = int(input('Enter a number from 1-5 to get an example '))
    figurative = figuratives[figurative_input-1]
except:
    print('You did not enter a figurative. Try again')


