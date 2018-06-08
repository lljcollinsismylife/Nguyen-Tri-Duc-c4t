our_items = ['T-shirts', 'Sweater']
action = input("Welcome to our shop,what do you want(C, R, U, D)?").upper()
if action == "R":
    print(our_items)
elif action == "C":
    new_item = input("Our new item is:")
    our_items.append(new_item)
    print(*our_items, sep=",")
elif action == "U":
    place = int(input("Update position?")) - 1
    new_item = input(" Our new item is:")
    our_items.insert(place, new_item)
    print(*our_items, sep=",")
elif action == "D":
    del our_items[int(input("Position to delete?")) - 1]
    print(our_items)

