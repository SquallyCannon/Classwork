def total_score(score, multiplier):
    return score * multiplier

def welcome():
    print("Welcome to the next level!")

score1 = total_score(3000,2)
score2 = total_score(2000,1.5)

welcome()
print(f"Your two scores are {score1} and {score2}.")

