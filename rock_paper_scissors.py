import random

quit = False
wins = 0
lose = 0
draw = 0

while not quit:
    comp_play = random.randrange(3)
    player_choice = int(input("Choose \n1. Rock \n2. Paper \n3. Scissors"))
    if not comp_play and player_choice == 1:
        print("You both chose rock: Draw!")
        draw += 1
    elif not comp_play and player_choice == 2:
        print("You chose Paper and computer chose Rock: You win!")
        wins += 1
    elif not comp_play and player_choice == 3:
        print("You chose Scissors and computer chose Rock: You lose!")
        lose =+ 1
    elif comp_play == 1 and player_choice == 1:
        print("You chose Rock and computer chose Paper: You lose!")
        lose =+ 1
    elif comp_play == 1 and player_choice == 2:
        print("You chose Paper and computer chose Paper: Draw!")
        draw += 1
    elif comp_play == 1 and player_choice == 3:
        print("You chose Scissors and computer chose Paper: You win!")
        wins += 1
    elif comp_play == 2 and player_choice == 1:
        print("You chose Rock and computer chose Scissors: You win!")
        wins += 1
    elif comp_play == 2 and player_choice == 2:
        print("You chose Paper and computer chose Scissors: You lose!")
        lose =+ 1
    elif comp_play == 2 and player_choice == 3:
        print("You chose Scissors and computer chose Scissors: Draw!")
        draw += 1
    else:
        print("Uh oh, something went wrong.")
    quit = int(input("Keep playing? \n0 for yes \n1 for no"))
print("Game has ended")
print("Final score:")
print("Wins:", wins)
print("Losses:", lose)
print("Draws:", draw)
print("Win percentage:", round(wins / (wins + lose + draw),2) * 100, "%")