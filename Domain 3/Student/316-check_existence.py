import os

if not os.path.exists('Python v2 Support Files/Domain 3/Student/316-message.txt'):
    message = open('Python v2 Support Files/Domain 3/Student/316-message.txt','w')
    message.write('Testing file for player configuration\n')
    message.write('Testing file for player score')
    print("Configuration file made \n" + "wow")
    message.close()
else: 
    message_test = open('Python v2 Support Files/Domain 3/Student/316-message.txt','r')
    content = message_test.read()
    print(content)
    message_test.close()