import random
import sys

choices = ["rock", "paper", "scissors", "lizard", "spock"]

def lost():
    computer_score = 0
    print("You lost!")
    computer_score += 1
    print(computer_score)

def draw():
    print("It´s a draw")
    
def win():
    player_score = 0
    print("You Won!")
    player_score += 1
    print(player_score)

def wrong():
    print("Please select a correct option")
    
def again():
    start = input("Do you want to play again? (y/n) ").lower()
    if start == "y":
        game()
    elif start == "n":
        print("Goodbye")
        sys.exit(0)
    else:
        wrong()
    
def start():
    while True:
        start = input("Do you want to play a game? (y/n) ").lower()
        if start == "y":
            game()
        elif start == "n":
            print("Goodbye")
            sys.exit(0)
        else:
            wrong()
                   
def game():
    player = input("Select your choice - Rock, Paper, Scissors, Lizard, Spock ")
    computer = random.choice(choices)
    if player in choices: 
        print(f"You selected {player} and the computer chose {computer}")
        if player == computer:
            draw()
        elif player == "rock" and computer == "scissors":
            win()
        elif player == "paper" and computer == "rock":
            win()
        elif player == "scissors" and computer == "paper":
            win()
        elif player == "lizard" and computer == "spock":
            win()
        elif player == "spock" and computer == "scissors":
            win()
        elif player == "rock" and computer == "lizard":
            win()
        elif player == "paper" and computer == "spock":
            win()
        elif player == "scissors" and computer == "lizard":
            win()
        elif player == "lizard" and computer == "paper":
            win()
        elif player == "spock" and computer == "rock":
            win()
        else:
            lost()
    else:
        wrong()    
    again()
          

start()