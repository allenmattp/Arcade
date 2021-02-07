import random

print("W E L C O M E\nT O\nC A M E L !\n")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run your pursuers!")

done = False
miles_traveled = 0
thirst = 0
camel_health = 0
natives = -20
canteen = random.randrange(5, 11)

while not done:
    if random.randrange(21) == 10:
        natives += random.randrange(1, 11)
        print("A sandstorm makes travel impossible!")
    if thirst > 2:
        print("Your throat is parched and you can only think of your thirst...")
    if camel_health > 4:
        print("Your camel stumbles as exhaustion wears it down...")
    if (miles_traveled - natives) < 16:
        print("You can hear your pursuers in the distance...")
    print("\n\nTHE DESERT SUN BEARS DOWN ON YOU... \n\n"
          "A. Drink from your canteen.\n"
          "B. Ahead at moderate pace. \n"
          "C. Full speed ahead! \n"
          "D. Stop to rest. \n"
          "E. Check your status. \n"
          "Q. Give up.\n")
    user_choice = input("What is your next move? ")
    if user_choice.lower() == "q":
        done = True
    elif user_choice.lower() == "e":
        print("You pause a moment to take stock of things...\n"
              "\n"
              "You estimate you've traveled", miles_traveled, "miles \n"
              "You have", canteen, "swigs left in your canteen\n"
              "You judge your pursuers are", miles_traveled - natives, "miles behind you...")
    elif user_choice.lower() == "d":
        camel_health = 0
        natives += random.randrange(7, 15)
        print("You stop to rest. Your camel is relieved.")
    elif user_choice.lower() == "c":
        camel_health += random.randrange(1, 4)
        thirst += 1
        miles_traveled += random.randrange(10, 21)
        natives += random.randrange(7, 15)
        if miles_traveled < 200:
            print("By the end of the day you estimate you'll have traveled", miles_traveled, "miles...")
    elif user_choice.lower() == "b":
        camel_health += 1
        thirst += 1
        miles_traveled += random.randrange(5, 13)
        natives += random.randrange(7, 15)
        if miles_traveled < 200:
            print("By the end of the day you estimate you'll have traveled", miles_traveled, "miles...")
    elif user_choice.lower() == "a":
        if canteen:
            thirst = 0
            canteen -= 1
            print("You take a drink... The water restores you!")
        else:
            thirst += 1
            print("You press the canteen to your lips but it is as dry as the desert...")
        natives += random.randrange(1, 6)

    if thirst >= 5:
        print("Your world spins as you are overcome by dehydration.\n"
              "You collapse as your consciousness forever slips away...")
        done = True
    if camel_health >= 8:
        print("Oh no! Your camel collapses from exhaustion.")
        done = True
    if natives >= miles_traveled:
        print("Oh no! The natives have caught you!")
        done = True
    if miles_traveled >= 200 and not done:
        print("It's not a mirage: You have escaped the desert!\n"
              "C O N G R A T U L A T I O N S\n"
              "Y O U\n"
              "W I N ! ! ! ! ! ! ! ! ! ! ! !")
        done = True
    if random.randrange(21) == 10 and user_choice.lower() != "e":
        thirst = 0
        camel_health = 0
        canteen = 10
        print("You've found an Oasis!\n"
              "You fill your canteen and both you and your camel are rested.")

print("Game over.")
