message = open('Python v2 Support Files/Domain 3/Student/314-message.txt','r+')
message.write('Testing file for player configuration :3 \n')
message.write('Testing file for player score')
content = message.read()
print(content)
message.close()

