import os
import questionary

inventorybaselister = {"Frozen Ham":50, "Frozen Turkey":50, "Canned Yams":5, "Canned Corn":5, "Canned Green beans":5, "Canned Carrots":5, "Canned Peas":5, "Canned Fruit":5, "Canned Pumpkin":5, "Canned Milk":5, "Instant Mashed Potatoes":8, "Potatoes":5, "Sugar":15, "Flour":10, "Cranberry Sauce":5, "Pie Crust":8, "Pie Filling":5, "Stuffing Mix":10, "Gravy Mix":1, "Bread mix":5, "Cookie Mix":5, "Cake Mix and Icing":5, "Cooking Oil":8, "Mac n Cheese":2}
inventorypantrylister = {"Canned Meats":10, "Peanut Butter":8, "Boxed Meal Kits":5, "Canned Soup":5, "Quick Meals":1}
#used for first boot and fixed point values

inventorybase = ("Frozen Ham", "Frozen Turkey", "Canned Yams", "Canned Corn", "Canned Green beans", "Canned Carrots", "Canned Peas", "Canned Fruit", "Canned Pumpkin", "Canned Milk", "Instant Mashed Potatoes", "Potatoes", "Sugar", "Flour", "Cranberry Sauce", "Pie Crust", "Pie Filling", "Stuffing Mix", "Gravy Mix", "Bread mix", "Cookie Mix", "Cake Mix and Icing", "Cooking Oil", "Mac n Cheese")
inventorypantry = ("Canned Meats", "Peanut Butter", "Boxed Meal Kits", "Canned Soup", "Quick Meals")
inventoryadd = []
#Used for refrence



if not os.path.exists('inventory.txt'):
    with open("inventory.txt", "a") as inventory:
        for item in inventorybaselister:
            inventory.write(f"{item}, 0 \n")
        inventory.write("\n")
        for item in inventorypantrylister:
            inventory.write(f"{item}, 0 \n")
        inventory.write("\n")
#First boot inventory.txt creator


def inventoryview():
    with open("inventory.txt", "r") as inventory:
        line2 = [line.strip() for line in inventory]
    line = 0
    total_points = 0
    total_items = 0
    for lined in line2:
        if lined == "":
            print("")
            continue
        if line <= 23:
            print(f"Item: {lined.split(", ")[0]} | Quantity: {lined.split(", ")[1]} | Point Value: {inventorybaselister[inventorybase[line]]} | {inventorybaselister[inventorybase[line]] * int(lined.split(", ")[1])}")
            total_points += inventorybaselister[inventorybase[line]] * int(lined.split(", ")[1])
            total_items += int(lined.split(", ")[1])
        elif line <= 28:
            print(f"Item: {lined.split(", ")[0]} | Quantity: {lined.split(", ")[1]} | Point Value: {inventorypantrylister[inventorypantry[line-24]]} | {inventorypantrylister[inventorypantry[line-24]] * int(lined.split(", ")[1])}")
            total_points += inventorypantrylister[inventorypantry[line-24]] * int(lined.split(", ")[1])
            total_items += int(lined.split(", ")[1])
        else:
            print(f"Item: {lined.split(", ")[0]} | Quantity: {lined.split(", ")[1]} | Point Value: 0 | Cumulative Points: 0")
            total_items += int(lined.split(", ")[1])
        line += 1
        print("")
    print(f"Total Points: {total_points} | Total Items: {total_items} \n")
#prints list of Item | Quantity | Point Value | Cumlative points

def search():
    continueing = True
    while continueing == True:
        with open("inventory.txt", "r") as inventory:
            line2 = [line.strip() for line in inventory]

        catalog = questionary.select(
            "Catalog:",
            choices=["Basket", "Pantry-only", "Other", "Back"],
        ).ask()

        if catalog == "Basket":
            basket = questionary.select(
            "Item:",
            inventorybase
            ).ask()
            for item in range(len(inventorybase)):
                if inventorybase[item] == basket:
                    basketid = item
            print(f"Item: {basket} | Quantity: {line2[basketid].split(", ")[1]} | Point Value: {inventorybaselister[basket]} | Cumulative Points: {int(line2[basketid].split(", ")[1]) * inventorybaselister[basket]}")
            continueing = False

        elif catalog == "Pantry-only":
            pantry = questionary.select(
                "Pantry:",
                inventorypantry
            ).ask()
            for item in range(len(inventorypantry)):
                if inventorypantry[item] == pantry:
                    pantryid = item+25
            print(f"Item: {pantry} | Quantity: {line2[pantryid].split(", ")[1]} | Point Value: {inventorypantrylister[pantry]} | Cumulative Points: {int(line2[pantryid].split(", ")[1]) * inventorypantrylister[pantry]}")
            continueing = False

        elif catalog == "Other":
            if len(inventoryadd) > 0:
                addition = questionary.select(
                    "Item:",
                    inventoryadd,
                ).ask()
                for item in range(len(inventoryadd)):
                    if inventoryadd[item] == addition:
                        additionid = item+31
                print(f"Item: {addition} | Quantity: {line2[additionid].split(", ")[1]} | Point Value: 0 | Cumulative Points: 0")
            else:
                print("There are no additive items to search for.")
            continueing = False
        else:
            continueing = False
#allows for searching using questionarys

def edit():
    continueing = True
    while continueing == True:
        with open("inventory.txt", "r") as inventory:
            targetline = inventory.readlines()
        editoption = questionary.select(
            "Select what you want to edit:",
            choices=["Add Quantity", "Remove Quantity", "Subtract Basket", "Add New Item", "Done"],
        ).ask()

        if editoption == "Add Quantity":
            editcatalog = questionary.select(
                "Select a Catalog:",
                choices=["Basket", "Pantry-only", "Other"],
            ).ask()

            if editcatalog == "Basket":
                basket = questionary.select(
                "Item:",
                inventorybase
                ).ask()
                for item in range(len(inventorybase)):
                    if inventorybase[item] == basket:
                        basketid = item
                        break

                basketadder = int(input("How many should be added: "))
                oldvalue = targetline[basketid].split(", ")[1]
                newvalue = f"{int(oldvalue) + basketadder} \n"

                if basketid < len(targetline):
                    targetline[basketid] = targetline[basketid].replace(oldvalue, newvalue)
                with open("inventory.txt", "w", encoding="utf-8") as inventory:
                    inventory.writelines(targetline)

                print(f"Item: {basket} | Quantity: {targetline[basketid].split(", ")[1].split("\n")[0]} | Point Value: {inventorybaselister[basket]} | Cumulative Points: {int(targetline[basketid].split(", ")[1]) * inventorybaselister[basket]}")

            elif editcatalog == "Pantry-only":
                pantry = questionary.select(
                    "Pantry:",
                    inventorypantry
                ).ask()
                for item in range(len(inventorypantry)):
                    if inventorypantry[item] == pantry:
                        pantryid = item+25

                pantryadder = int(input("How many should be added: "))
                oldvalue = targetline[pantryid].split(", ")[1]
                newvalue = f"{int(oldvalue) + pantryadder} \n"

                if pantryid < len(targetline):
                    targetline[pantryid] = targetline[pantryid].replace(oldvalue, newvalue)
                with open("inventory.txt", "w", encoding="utf-8") as inventory:
                    inventory.writelines(targetline)

                print(f"Item: {pantry} | Quantity: {targetline[pantryid].split(", ")[1].split("\n")[0]} | Point Value: {inventorypantrylister[pantry]} | Cumulative Points: {int(targetline[pantryid].split(", ")[1]) * inventorypantrylister[pantry]}")

            elif editcatalog == "Other":
                if len(inventoryadd) > 0:
                    addition = questionary.select(
                        "Item:",
                        inventoryadd,
                    ).ask()
                    for item in range(len(inventoryadd)):
                        if inventoryadd[item] == addition:
                            additionid = item+31

                    additionadder = int(input("How many should be added: "))
                    oldvalue = targetline[additionid].split(", ")[1]
                    newvalue = f"{int(oldvalue) + additionadder} \n"

                    if additionid < len(targetline):
                        targetline[additionid] = targetline[additionid].replace(oldvalue, newvalue)
                    with open("inventory.txt", "w", encoding="utf-8") as inventory:
                        inventory.writelines(targetline)

                    print(f"Item: {addition} | Quantity: {targetline[additionid].split(", ")[1].split("\n")[0]} | Point Value: 0 | Cumulative Points: 0")
                else:
                    print("There are no additive items to edit.")

        elif editoption == "Remove Quantity":
            editcatalog = questionary.select(
                "Select a Catalog:",
                choices=["Basket", "Pantry-only", "Other"],
            ).ask()

            if editcatalog == "Basket":
                basket = questionary.select(
                "Item:",
                inventorybase
                ).ask()
                for item in range(len(inventorybase)):
                    if inventorybase[item] == basket:
                        basketid = item
                        break

                basketadder = int(input("How many should be added: "))
                oldvalue = targetline[basketid].split(", ")[1]
                newvalue = f"{int(oldvalue) - basketadder} \n"

                if not int(newvalue) < 0:
                    if basketid < len(targetline):
                        targetline[basketid] = targetline[basketid].replace(oldvalue, newvalue)
                    with open("inventory.txt", "w", encoding="utf-8") as inventory:
                        inventory.writelines(targetline)
                else:
                    print("You attempted to remove more items than exist.")

                print(f"Item: {basket} | Quantity: {targetline[basketid].split(", ")[1].split("\n")[0]} | Point Value: {inventorybaselister[basket]} | Cumulative Points: {int(targetline[basketid].split(", ")[1]) * inventorybaselister[basket]}")

            elif editcatalog == "Pantry-only":
                pantry = questionary.select(
                    "Pantry:",
                    inventorypantry
                ).ask()
                for item in range(len(inventorypantry)):
                    if inventorypantry[item] == pantry:
                        pantryid = item+25

                pantryadder = int(input("How many should be added: "))
                oldvalue = targetline[pantryid].split(", ")[1]
                newvalue = f"{int(oldvalue) - pantryadder} \n"

                if not int(newvalue) < 0:
                    if pantryid < len(targetline):
                        targetline[pantryid] = targetline[pantryid].replace(oldvalue, newvalue)
                    with open("inventory.txt", "w", encoding="utf-8") as inventory:
                        inventory.writelines(targetline)
                else:
                    print("You attempted to remove more items than exist.")

                print(f"Item: {pantry} | Quantity: {targetline[pantryid].split(", ")[1].split("\n")[0]} | Point Value: {inventorypantrylister[pantry]} | Cumulative Points: {int(targetline[pantryid].split(", ")[1]) * inventorypantrylister[pantry]}")

            elif editcatalog == "Other":
                if len(inventoryadd) > 0:
                    addition = questionary.select(
                        "Item:",
                        inventoryadd,
                    ).ask()
                    for item in range(len(inventoryadd)):
                        if inventoryadd[item] == addition:
                            additionid = item+31

                    additionadder = int(input("How many should be added: "))
                    oldvalue = targetline[additionid].split(", ")[1]
                    newvalue = f"{int(oldvalue) - additionadder} \n"

                    if not int(newvalue) < 0:
                        if additionid < len(targetline):
                            targetline[additionid] = targetline[additionid].replace(oldvalue, newvalue)
                        with open("inventory.txt", "w", encoding="utf-8") as inventory:
                            inventory.writelines(targetline)
                            print(f"Item: {addition} | Quantity: {targetline[additionid].split(", ")[1].split("\n")[0]} | Point Value: 0 | Cumulative Points: 0")
                    else:
                        print("You attempted to remove more items than exist.")
                else:
                    print("There are no additive items to edit.") 

        else:
            continueing = False
        

        '''elif editoption == "Subtract Basket":

        elif editoption == "Add New Item":'''
#used for adding or subracting quantity, removing 1 basket, or adding a new item

def baskets():
    basketpos = True
    basket = 0
    required = 1
    lowest = []
    while basketpos == True:
        with open("inventory.txt", "r") as inventory:
            line2 = [line.strip() for line in inventory]
        for item in range(len(inventorybase)):
            if int(line2[item].split(", ")[1]) < required:
                basketpos = False
                lowest.append(inventorybase[item])
        if basketpos == True:
            required +=1
            basket += 1
    print("")
    print("The limiting items are:")
    for low in lowest:
        print(low)
    print("")
    print(f"We can make {basket} Baskets with the current inventory.")
    print("")

operation = True
while operation == True:
    command = questionary.select(
        "Please select a command:",
        choices=["View Inventory", "Search", "Edit", "Baskets", "Top/Bottom 5", "Show log","Close"],
    ).ask()

    print(f"You selected: {command}")
    if command == "View Inventory":
        inventoryview()
    elif command == "Search":
        search()
    elif command == "Edit":
        edit()
    elif command == "Baskets":
        baskets()
    elif command == "Close":
        operation = False
