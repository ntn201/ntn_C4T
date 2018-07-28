action_list = ["C", "R", "U", "D", "c", "r", "u", "d", "E", "e"]
items = ["Pham Minh Duc", "Do Huu An", "Nguyen Tran Nguyen"]
end = False
while not end:
    action = input(
        "Welcome to our shop, what do you want (C, R, U, D)?, enter E to exit ")
    if action not in action_list:
        print("You entered wrong action")
    elif (action == "C" or action == "c"):
        new_item = input("Enter new item: ")
        items.append(new_item)
        print("Our item:", *items,sep = ", ")
    elif (action == "R" or action == "r"):
       print("Our item:", *items,sep = ", ")
    elif (action == "U" or action == "u"):
        position = int(input("Update position? ")) - 1
        if position > len(items):
            print("You entered wrong position")
        else:
            new_item = input("Enter new item: ")
            items[position] = new_item
            print("Our item:", *items,sep = ", ")
    elif (action == "D" or action == "d"):
        position = int(input("Delete position? ")) - 1
        if position > len(items):
            print("You entered wrong position")
        else:
            items.pop(position)
            print("Our item:", *items,sep = ", ")
    elif (action == "E" or action == "e"):
        end = True
