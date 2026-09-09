import os
message_file = 'Python v2 Support Files/Domain 3/Student/317-message.txt'

if os.path.exists(message_file):
    os.remove(message_file)
    print("Message file removed")
    
else: 
    print("There was no message file to remove")
    message_file = open('Python v2 Support Files/Domain 3/Student/317-message.txt','w')
    message_file.write('Testing file for player configuration\n')
    message_file.write('Testing file for player score')
    print("Configuration file made \n" + "wow")
    message_file.close()