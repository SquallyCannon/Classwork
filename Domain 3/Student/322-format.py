score = 200000
level = 3
player1 = "Stacey"

print("Player1:", player1, "| Score:", score, "| Level:", level)
print("{} has {} points and has reached level {}".format(player1,score,level))
print("{2} has {0} points and has reached level {1}".format(score,level,player1))
print(f"{player1} has {score} points and has reached level {level}")
print(f"{player1:<15} {score:>10}")
print("Player1: %1s | Score: %.2f" % (player1, score))