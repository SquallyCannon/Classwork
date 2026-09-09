message = open('Python v2 Support Files/Domain 3/Student/313-message.txt','w')
message.write('Testing file for player configuration :3 \n')
message.write('Testing file for player score')
message.close()

message_test = open('Python v2 Support Files/Domain 3/Student/313-message.txt','r+')
content = message_test.read()
print(content)
message_test.close()