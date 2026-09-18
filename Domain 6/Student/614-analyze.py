import io

question_stream = io.StringIO()

question_stream.write("The game has started.\n")
question_stream.write("Here is your first question. \n")
question_stream.write("What is the formula for the area of a circle?")

question_stream.seek(0)
print(question_stream.read())