import datetime
current_time = datetime.datetime.now()
print("The current date and time is:", current_time.strftime("%m-%d-%Y %H:%M %p"))# date in mm-dd-yy)
print("The current weekday number is:", current_time.weekday())
print("The current weekday is:", current_time.strftime("%A"))
