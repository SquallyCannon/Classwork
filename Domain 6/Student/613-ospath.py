import os.path

if not os.path.exists('613-message.txt'):
    message = open('613-message.txt','w')
    message.write('Testing file for player configuration\n')
    message.write('Testing file for player score')
    print("Configuration file made")
    message.close()
else: 
    message_test = open('613-message.txt','r')
    content = message_test.read()
    print(content)
    message_test.close()

    file_path = os.path.join('613-test', '613-test.txt')
    if os.path.exists(file_path):
        print("Exists")