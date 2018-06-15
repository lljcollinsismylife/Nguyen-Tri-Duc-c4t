map = {
     "size_x": 9,
     "size_y": 9
 }


player = {
    "x":4,
    "y":4
}
boxes = [
    {"x": 1, "y":1},
    {"x": 2, "y": 2},
    {"x":3, "y": 3}
]

destinations = [
    {"x": 2, "y": 1},
    {"x": 4, "y": 3},
    {"x": 2, "y": 4}
]
obstacle = [
    {"x": 3, "y": 1},
    {"x": 3, "y": 2},
    {"x": 1, "y": 3}
]

while True:
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            player_is_here = False
            box_is_here = False
            dest_is_here = False
            obs_is_here = False

            for obs in obstacle:
                if obs["x"] == x and obs["y"] == y:
                    obs_is_here = True
                    break
            for dest in destinations:
                if dest["x"] == x and dest["y"] == y:
                    dest_is_here = True
                    break
            for box in boxes:
                if box["x"] == x and box["y"] == y:
                    box_is_here = True
                    break



            if x == player["x"] and y == player["y"]:
                player_is_here = True


            if player_is_here is True:
                print("p ", end="")
            elif box_is_here is True:
                print("B ", end="")
            elif dest_is_here is True:
                print("D ", end="")
            elif obs_is_here is True:
                print("O ", end="")
            else:
                print("- ", end="")

        print()

        win = True
        for box in boxes:
            if box not in destinations:
                win = False

        if win:
            print("You win")
            break


    move = input("Ur move:?").upper()

    dx = 0
    dy = 0
    if move == 'W':
        print("Up")
        dy = -1
    elif move == "A":
        print("Left")
        dx = -1
    elif move == "S":
        print("Down")
        dy = 1
    elif move == "D":
        print("Right")
        dx = 1
    elif move == "UNDO":
        dx = -dx
        dy = -dy
        undo = True
    elif move == "QUIT":
        print('Game over!!!!')
        break
    else:
        print("Ezzzz")
        break
    if 0 <= player["x"] + dx < map["size_x"] and 0 <= player["y"] + dy <= map["size_y"]:
        player["x"] += dx
        player["y"] += dy

    for box in boxes:
        if box["x"] == player["x"] and box["y"] == player ["y"]:
            box["x"] += dx
            box["y"] += dy
    for box in boxes:
        if player["x"] == box["x"] and player["y"] == box["y"]:
            player["x"] -= dx
            player["y"] -= dy
    for obs in obstacle:
        for box in boxes:
            if box['x'] == obs["x"] and box['y'] == obs["y"]:
                box['x'] -= dx
                box['y'] -= dy
                player["x"] -= dx
                player["y"] -= dy



