import random

start = input("Would you like to play the computer (y/n)")

while(start == "y"):
    cpu_selection = ["rock", "paper", "scissor"]
    player_1 = input("player 1 please enter your name: ")

    p1_selection = input(player_1 + " please select rock, paper or scissor: ")
    computer = random.choice(cpu_selection)
    print("computer chose: " + computer)
    if(p1_selection == "rock" and computer == "scissors"):
        print(player_1 + " is the winer")
    elif(p1_selection == "paper" and computer == "rock"):
        print(player_1 + " is the winner")
    elif(p1_selection == "scissor" and computer == "paper"):
        print(player_1 + " is the winner")
    elif(p1_selection == computer):
        print("It's a draw")
    else:
        print("computer wins")
    start = input("Would you like to play the computer again (y/n)")

print("Sorry you dont want to play...goodbye")
