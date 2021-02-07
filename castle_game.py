done = False

room_list = []
format = ["description", "north", "east", "south", "west"
          ]
room = ["Once full of visitors and subjects, the castle's entrance is now covered in a thick layer of dust.",
        3, 6, 8, 1]  # 0
room_list.append(room)
room = ["This hallway was frequented by commoners and workstaff. It is bare but functional.",
        2, 0, None, None]  # 1
room_list.append(room)
room = ["The stench of rotting food pervades the air. A feast, mid-prep, sits abandoned.",
        None, 3, 1, None]  # 2
room_list.append(room)
room = ["In the past the grandeur of the Court Room would evoke awe, but today you feel only despair.",
        4, 5, 0, 2]  # 3
room_list.append(room)
room = ["The courtyard's garden is overtaken by weeds. "
        "You catch a flash of movement as something disappears into the brambles.",
        None, None, 3, None]  # 4
room_list.append(room)
room = ["The walls are arrayed with ancient texts, many unopened far longer than the castle has been abandoned."
        "The wind cuts through the room although there are no windows.",
        7, None, 6, 3]  # 5
room_list.append(room)
room = ["This hall was restricted to scholars and favored subjects. Stone busts watch you with skeptical eyes.",
        5, None, None, 0]  # 6
room_list.append(room)
room = ["You've discovered a secret room! You spy the MacGuffin sitting unguarded on a shelf.",
        None, None, None, 5]  # 7
room_list.append(room)
room = ["You stand outside the old castle, its walls forboding but the gate open. Dare you enter?",
        0, None, None, None]  # 8
room_list.append(room)

current_room = 8

while not done:
    print()
    print(room_list[current_room][0])
    user = input("What do you do? \n Look, North, East, South, West, Quit.")
    if user.lower()[0] == "q":
        print("\nYou abandon your adventure.\nG O O D B Y E")
        done = True

    if user.lower()[0] == "l":
        print("\nYou examine your surroundings:\n")
        if room_list[current_room][1] != None:
            print("There is a way North.")
        if room_list[current_room][2] != None:
            print("There is a way East.")
        if room_list[current_room][3] != None:
            print("There is a way South.")
        if room_list[current_room][4] != None:
            print("There is a way West.")

    if user.lower()[0] == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("There is nothing that way...")
        else:
            current_room = next_room

    if user.lower()[0] == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("There is nothing that way...")
        else:
            current_room = next_room

    if user.lower()[0] == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("There is nothing that way...")
        else:
            current_room = next_room

    if user.lower()[0] == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("There is nothing that way...")
        else:
            current_room = next_room