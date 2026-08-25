#dictionary example
coins = {
    "gold":2,
    "silver":3,
    "bronze":0
}

conversion = 10
#print(coins)

while coins["bronze"] > conversion-1:
    coins["bronze"] -= conversion
    coins["silver"] += 1

while coins["silver"] > conversion-1:
    coins["silver"] -= conversion
    coins["gold"] += 1

#print("Gold:", coins["gold"], "| Silver:" , coins["silver"], "| Bronze:", coins["bronze"])

coins["bronze"] -=11

while coins["bronze"] <= 0 or coins["silver"] <= 0:
    if coins["bronze"] <= 0 and coins["silver"] > 0:
        coins["silver"] -=1
        coins["bronze"] += conversion

    if coins["bronze"] <= 0 and coins["silver"] <= 0 and coins["gold"] > 0:
        coins["gold"] -=1
        coins["silver"] += conversion
        coins["silver"] -=1
        coins["bronze"] += conversion
    if coins["bronze"] <= 0 and coins["silver"] <= 0 and coins["gold"] <= 0:
        print("You went bankrupt")

#print("Gold:", coins["gold"], "| Silver:" , coins["silver"], "| Bronze:", coins["bronze"])

coins = {
    "platinum":1,
    "gold":coins["gold"],
    "silver":coins["silver"],
    "bronze":coins["bronze"]
}
#print("Platinum:", coins["platinum"], "| Gold:", coins["gold"], "| Silver:" , coins["silver"], "| Bronze:", coins["bronze"])

#set example
regions = {"north","south","east"}
regions.add("west")

#print(regions)

#tuple example
char1_name=("Humphrey",'Cat')
dog = char1_name[1]
print(dog)