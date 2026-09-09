with open("Python v2 Support Files/Domain 3/Student/323-message-items.txt", "r") as itemsm:
    itemst = itemsm.read()

items = [itemst[1:5], itemst[7:11], itemst[13:-1]]

for item in items[1:]:
    print(f"You can get a {item} at level 1")
for item in items:
    if item == "Rock":
        continue
    else:
        print(f"You can get a {item} at level 2")
for item in items:
    print(f"You can get a {item} at level 3")