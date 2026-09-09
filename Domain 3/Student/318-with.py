'''message = open('Python v2 Support Files/Domain 3/Student/318-message.txt','w')
message.write('Testing file for player configuration\n')
message.write('Testing file for player score\n')
message.close()'''

with open('Python v2 Support Files/Domain 3/Student/318-with.py','w') as message:
    message.write('"Testing file for player configuration"\n')
    message.write('"Testing file for player score"\n')
    print("file created")