score = 0
score_increase = 2
score_exponent = 1
score_test = 10
round = 0

while score <= 1000000000000:
   round += 1
   print("You have", score, "points.") 
   score += score_increase
   if score > 10**(score_exponent-1):
      score_increase += 10**score_exponent
      score_exponent += 1

print("You have", score, "points.")
print("Score increases by: ", score_increase)
print(round)

