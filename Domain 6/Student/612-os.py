import os

print("Your current directory is:", os.getcwd())

for text_file in os.listdir():
    if text_file.endswith('.txt'):
        print(text_file)

os.rename('601-message.txt', 'OLD601-message.txt')

for text_file in os.listdir():
    if text_file.endswith('.txt'):
        print(text_file)



