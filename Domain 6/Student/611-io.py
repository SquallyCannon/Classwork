import io

game_stream = io.StringIO()

game_stream.write("The game has started.\n")
game_stream.write("Here is your first question. \n")

game_stream.seek(22)
print(game_stream.read())