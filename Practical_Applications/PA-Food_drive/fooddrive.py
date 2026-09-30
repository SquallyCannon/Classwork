import os
import questionary
import datetime

inventorybaselister = {"Frozen Ham":50, "Frozen Turkey":50, "Canned Yams":5, "Canned Corn":5, "Canned Green beans":5, "Canned Carrots":5, "Canned Peas":5, "Canned Fruit":5, "Canned Pumpkin":5, "Canned Milk":5, "Instant Mashed Potatoes":8, "Potatoes":5, "Sugar":15, "Flour":10, "Cranberry Sauce":5, "Pie Crust":8, "Pie Filling":5, "Stuffing Mix":10, "Gravy Mix":1, "Bread mix":5, "Cookie Mix":5, "Cake Mix and Icing":5, "Cooking Oil":8, "Mac n Cheese":2}
inventorypantrylister = {"Canned Meats":10, "Peanut Butter":8, "Boxed Meal Kits":5, "Canned Soup":5, "Quick Meals":1}
#used for first boot and fixed point values

inventorybase = ("Frozen Ham", "Frozen Turkey", "Canned Yams", "Canned Corn", "Canned Green beans", "Canned Carrots", "Canned Peas", "Canned Fruit", "Canned Pumpkin", "Canned Milk", "Instant Mashed Potatoes", "Potatoes", "Sugar", "Flour", "Cranberry Sauce", "Pie Crust", "Pie Filling", "Stuffing Mix", "Gravy Mix", "Bread mix", "Cookie Mix", "Cake Mix and Icing", "Cooking Oil", "Mac n Cheese")
inventorypantry = ("Canned Meats", "Peanut Butter", "Boxed Meal Kits", "Canned Soup", "Quick Meals")
inventoryadd = []
#Used for refrence

months = ["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
#month names


if not os.path.exists('inventory.txt'):
    with open("inventory.txt", "a") as inventory:
        for item in inventorybaselister:
            inventory.write(f"{item}, 0 \n")
        inventory.write("\n")
        for item in inventorypantrylister:
            inventory.write(f"{item}, 0 \n")
        inventory.write("\n")
#First boot inventory.txt creator

with open("inventory.txt", "r") as inventory:
    line2 = [line.strip() for line in inventory]
for line in range(len(line2)):
    if line > 30:
        inventoryadd.append(line2[line].split(", ")[0])
#Refresh additional items


def inventoryview():
    with open("inventory.txt", "r") as inventory:
        line2 = [line.strip() for line in inventory]
    line = 0
    total_points = 0
    total_items = 0
    print("")
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
            choices=["Add Quantity", "Remove Quantity", "Add Basket", "Subtract Basket", "Add New Custom Item","Remove Custom Item", "Done"],
        ).ask()

        if editoption == "Add Quantity":
            editcatalog = questionary.select(
                "Select a Catalog:",
                choices=["Basket", "Pantry-only", "Other", "Back"],
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
                try:
                    basketadder = int(input("How many should be added: "))
                except:
                    raise ValueError("Input must be an Integer")
                    basketadder = 0
                oldvalue = targetline[basketid].split(", ")[1]
                newvalue = f"{int(oldvalue) + basketadder} \n"

                if basketid < len(targetline):
                    targetline[basketid] = targetline[basketid].replace(oldvalue, newvalue)
                with open("inventory.txt", "w", encoding="utf-8") as inventory:
                    inventory.writelines(targetline)

                print(f"Item: {basket} | Quantity: {targetline[basketid].split(", ")[1].split("\n")[0]} | Point Value: {inventorybaselister[basket]} | Cumulative Points: {int(targetline[basketid].split(", ")[1]) * inventorybaselister[basket]}")
                with open("transactions.txt", "a") as transaction:
                    time = datetime.datetime.now()
                    month = months[time.month - 1]
                    transaction.write(month)
                    transaction.write(f"{time.strftime("-%d-%Y %H:%M %p")} | UPDATE | Added quantity {basketadder} | {basket} - {targetline[basketid].split(", ")[1].split("\n")[0]} \n")

            elif editcatalog == "Pantry-only":
                pantry = questionary.select(
                    "Pantry:",
                    inventorypantry
                ).ask()
                for item in range(len(inventorypantry)):
                    if inventorypantry[item] == pantry:
                        pantryid = item+25

                try:
                    pantryadder = int(input("How many should be added: "))
                except:
                    raise ValueError("Input must be an Integer")
                    pantryadder = 0
                oldvalue = targetline[pantryid].split(", ")[1]
                newvalue = f"{int(oldvalue) + pantryadder} \n"

                if pantryid < len(targetline):
                    targetline[pantryid] = targetline[pantryid].replace(oldvalue, newvalue)
                with open("inventory.txt", "w", encoding="utf-8") as inventory:
                    inventory.writelines(targetline)

                print(f"Item: {pantry} | Quantity: {targetline[pantryid].split(", ")[1].split("\n")[0]} | Point Value: {inventorypantrylister[pantry]} | Cumulative Points: {int(targetline[pantryid].split(", ")[1]) * inventorypantrylister[pantry]}")
                with open("transactions.txt", "a") as transaction:
                    time = datetime.datetime.now()
                    month = months[time.month - 1]
                    transaction.write(month)
                    transaction.write(f"{time.strftime("-%d-%Y %H:%M %p")} | UPDATE | Added quantity {pantryadder} | {pantry} - {targetline[pantryid].split(", ")[1].split("\n")[0]} \n")

            elif editcatalog == "Other":
                if len(inventoryadd) > 0:
                    addition = questionary.select(
                        "Item:",
                        inventoryadd,
                    ).ask()
                    for item in range(len(inventoryadd)):
                        if inventoryadd[item] == addition:
                            additionid = item+31

                    try:
                        additionadder = int(input("How many should be added: "))
                    except:
                        raise ValueError("Input must be an Integer")
                        additionadder = 0
                    oldvalue = targetline[additionid].split(", ")[1]
                    newvalue = f"{int(oldvalue) + additionadder} \n"

                    if additionid < len(targetline):
                        targetline[additionid] = targetline[additionid].replace(oldvalue, newvalue)
                    with open("inventory.txt", "w", encoding="utf-8") as inventory:
                        inventory.writelines(targetline)

                    print(f"Item: {addition} | Quantity: {targetline[additionid].split(", ")[1].split("\n")[0]} | Point Value: 0 | Cumulative Points: 0")
                    with open("transactions.txt", "a") as transaction:
                        time = datetime.datetime.now()
                        month = months[time.month - 1]
                        transaction.write(month)
                        transaction.write(f"{time.strftime("-%d-%Y %H:%M %p")} | UPDATE | Added quantity {additionadder} | {addition} - {targetline[additionid].split(", ")[1].split("\n")[0]} \n")
                else:
                    print("There are no additive items to edit.")

        elif editoption == "Remove Quantity":
            editcatalog = questionary.select(
                "Select a Catalog:",
                choices=["Basket", "Pantry-only", "Other", "Back"],
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

                try:
                    basketadder = int(input("How many should be added: "))
                except:
                    raise ValueError("Input must be an Integer")
                    basketadder = 0
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
                with open("transactions.txt", "a") as transaction:
                    time = datetime.datetime.now()
                    month = months[time.month - 1]
                    transaction.write(month)
                    transaction.write(f"{time.strftime("-%d-%Y %H:%M %p")} | UPDATE | Subtracted quantity {basketadder} | {basket} - {targetline[basketid].split(", ")[1].split("\n")[0]} \n")

            elif editcatalog == "Pantry-only":
                pantry = questionary.select(
                    "Pantry:",
                    inventorypantry
                ).ask()
                for item in range(len(inventorypantry)):
                    if inventorypantry[item] == pantry:
                        pantryid = item+25

                try:
                    pantryadder = int(input("How many should be added: "))
                except:
                    raise ValueError("Input must be an Integer")
                    pantryadder = 0
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
                with open("transactions.txt", "a") as transaction:
                    time = datetime.datetime.now()
                    month = months[time.month - 1]
                    transaction.write(month)
                    transaction.write(f"{time.strftime("-%d-%Y %H:%M %p")} | UPDATE | Subtracted quantity {pantryadder} | {pantry} - {targetline[pantryid].split(", ")[1].split("\n")[0]} \n")

            elif editcatalog == "Other":
                if len(inventoryadd) > 0:
                    addition = questionary.select(
                        "Item:",
                        inventoryadd,
                    ).ask()
                    for item in range(len(inventoryadd)):
                        if inventoryadd[item] == addition:
                            additionid = item+31

                    try:
                        additionadder = int(input("How many should be added: "))
                    except:
                        raise ValueError("Input must be an Integer")
                        additionadder = 0
                    oldvalue = targetline[additionid].split(", ")[1]
                    newvalue = f"{int(oldvalue) - additionadder} \n"

                    if not int(newvalue) < 0:
                        if additionid < len(targetline):
                            targetline[additionid] = targetline[additionid].replace(oldvalue, newvalue)
                        with open("inventory.txt", "w", encoding="utf-8") as inventory:
                            inventory.writelines(targetline)
                            print(f"Item: {addition} | Quantity: {targetline[additionid].split(", ")[1].split("\n")[0]} | Point Value: 0 | Cumulative Points: 0")
                            with open("transactions.txt", "a") as transaction:
                                time = datetime.datetime.now()
                                month = months[time.month - 1]
                                transaction.write(month)
                                transaction.write(f"{time.strftime("-%d-%Y %H:%M %p")} | UPDATE | Subtracted quantity {additionadder} | {addition} - {targetline[additionid].split(", ")[1].split("\n")[0]} \n")
                    else:
                        print("You attempted to remove more items than exist.")
                else:
                    print("There are no additive items to edit.") 
        
        elif editoption == "Add Basket":
            for item in range(len(inventorybase)):
                oldvalue = targetline[item].split(", ")[1]
                newvalue = f"{int(oldvalue) + 1} \n"

                if item < len(targetline):
                    targetline[item] = targetline[item].replace(oldvalue, newvalue)
                with open("inventory.txt", "w", encoding="utf-8") as inventory:
                    inventory.writelines(targetline)
            with open("transactions.txt", "a") as transaction:
                time = datetime.datetime.now()
                month = months[time.month - 1]
                transaction.write(month)
                transaction.write(f"{time.strftime("-%d-%Y %H:%M %p")} | UPDATE | Added Full Basket | All +1 \n")
                    
        elif editoption == "Subtract Basket":
            basketpos = True
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
                    for item2 in range(len(inventorybase)):
                        oldvalue = targetline[item2].split(", ")[1]
                        newvalue = f"{int(oldvalue) - 1} \n"
                                
                        if not int(newvalue) < 0:
                            if item2 < len(targetline):
                                targetline[item2] = targetline[item2].replace(oldvalue, newvalue)
                            with open("inventory.txt", "w", encoding="utf-8") as inventory:
                                inventory.writelines(targetline)
                        else:
                            print("Error")
                    with open("transactions.txt", "a") as transaction:
                        time = datetime.datetime.now()
                        month = months[time.month - 1]
                        transaction.write(month)
                        transaction.write(f"{time.strftime("-%d-%Y %H:%M %p")} | UPDATE | Subtracted Full Basket | All -1 \n")
                    basketpos = False
                else:
                    print(f"There are not enough {lowest} to subtract a basket")
        
        elif editoption == "Add New Custom Item":
            failcreate = False
            newitem = input("The name of the new item: ")
            try:
                newitemamount = int(input("How many of this item: "))
                if newitemamount < 0:
                    newitemamount /=0
            except:
                print("Values must be integers and positive.")
                failcreate = True
            if failcreate == False:
                with open("inventory.txt", "a") as inventory:
                    inventory.write(f"{newitem}, {newitemamount}")
                    inventory.write("\n")
                    inventoryadd.append(newitem)
                with open("transactions.txt", "a") as transaction:
                    time = datetime.datetime.now()
                    month = months[time.month - 1]
                    transaction.write(month)
                    transaction.write(f"{time.strftime("-%d-%Y %H:%M %p")} | UPDATE | Added New Item {newitem} | {newitem} - {newitemamount} \n")

        elif editoption == "Remove Custom Item":
            faildelete = False
            if len(inventoryadd) > 0:
                customitem = questionary.select(
                    "Item:",
                    inventoryadd,
                ).ask()
                for item in range(len(inventoryadd)):
                    if inventoryadd[item] == customitem:
                        additionid = item+31
            else:
                print("There are no additive items to remove.")
                faildelete = True
            if faildelete == False:
                with open("inventory.txt", "w") as inventory:
                    for index, line in enumerate(targetline):
                        if index != additionid:
                            inventory.write(f"{line}")
                inventoryadd.pop(additionid-31)
                with open("transactions.txt", "a") as transaction:
                    time = datetime.datetime.now()
                    month = months[time.month - 1]
                    transaction.write(month)
                    transaction.write(f"{time.strftime("-%d-%Y %H:%M %p")} | UPDATE | Removed Custom Item {customitem} | {customitem} - None \n")

        else:
            continueing = False    
#used for adding or subracting quantity, adding/removing 1 basket, or adding/removing a custom item

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
#returns how many baskets can be made with current quantities

def ranking():
    rankn = []
    rankv = []
    best1 = None
    best2 = None
    best3 = None
    best4 = None
    best5 = None
    worst1 = None
    worst2 = None
    worst3 = None
    worst4 = None
    worst5 = None
    with open("inventory.txt", "r") as inventory:
        targetline = inventory.readlines()
    for line in range(len(inventorybase)):
        vline = int(targetline[line].split(", ")[1])
        nline = targetline[line].split(", ")[0]
        rankn.append(nline)
        rankv.append(vline)
    rankv.sort(reverse=True)
    for line in range(len(inventorybase)):
        if rankv[0] == int(targetline[line].split(", ")[1]) and best1 == None:
            best1 = targetline[line].split(", ")[0]
        elif rankv[1] == int(targetline[line].split(", ")[1]) and best2 == None:
            best2 = targetline[line].split(", ")[0]
        elif rankv[2] == int(targetline[line].split(", ")[1]) and best3 == None:
            best3 = targetline[line].split(", ")[0]
        elif rankv[3] == int(targetline[line].split(", ")[1]) and best4 == None:
            best4 = targetline[line].split(", ")[0]
        elif rankv[4] == int(targetline[line].split(", ")[1]) and best5 == None:
            best5 = targetline[line].split(", ")[0]

        elif rankv[-1] == int(targetline[line].split(", ")[1]) and worst1 == None:
            worst1 = targetline[line].split(", ")[0]
        elif rankv[-2] == int(targetline[line].split(", ")[1]) and worst2 == None:
            worst2 = targetline[line].split(", ")[0]
        elif rankv[-3] == int(targetline[line].split(", ")[1]) and worst3 == None:
            worst3 = targetline[line].split(", ")[0]
        elif rankv[-4] == int(targetline[line].split(", ")[1]) and worst4 == None:
            worst4 = targetline[line].split(", ")[0]
        elif rankv[-5] == int(targetline[line].split(", ")[1]) and worst5 == None:
            worst5 = targetline[line].split(", ")[0]

        else:
            continue
    print("")

    print(f"The top 5 are:")
    print(f"1: {best1} with {rankv[0]}")
    print(f"2: {best2} with {rankv[1]}")
    print(f"3: {best3} with {rankv[2]}")
    print(f"4: {best4} with {rankv[3]}")
    print(f"5: {best5} with {rankv[4]}")  
    print("")
    print(f"The bottom 5 are:")
    print(f"1: {worst1} with {rankv[-1]}")
    print(f"2: {worst2} with {rankv[-2]}")
    print(f"3: {worst3} with {rankv[-3]}")
    print(f"4: {worst4} with {rankv[-4]}")
    print(f"5: {worst5} with {rankv[-5]}")
#returns top 5 quantities and bottom 5 quantities

def log():
    print("")
    with open("transactions.txt", "r") as transaction:
        trans = transaction.readlines()
        for line in trans:
            print(line)
#returns transactionlog

operation = True
while operation == True:
    command = questionary.select(
        "Please select a command:",
        choices=["View Inventory", "Search", "Edit", "Baskets", "Top/Bottom 5", "Show Transaction Log","Close"],
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
    elif command == "Top/Bottom 5":
        ranking()
    elif command == "Show Transaction Log":
        log()
    else:
        operation = False
