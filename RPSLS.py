import random
import sys

choices = ["rock", "paper", "scissors", "lizard", "spock"]
computer_score = 0
player_score = 0
count = 0
    
def lost(computer_score):
    print("You lost!")
    computer_score += 1
    return computer_score

def draw():
    print("It´s a draw")
    
def win(player_score):
    print("You Won!")
    player_score += 1
    return player_score

def wrong():
    print("Please select a correct option")
    
def again(count):
    start = input("Do you want to play again? (y/n) ").lower()
    if start == "y":
        count += 1
        game(count)
    elif start == "n":
        print("Goodbye")
        sys.exit(0)
    else:
        wrong()
    
def start(count = 0):
    while True:
        start = input("Do you want to play a game? (y/n) ").lower()
        if start == "y":
            count += 1
            game(count)
        elif start == "n":
            print("Goodbye")
            sys.exit(0)
        else:
            wrong()
        return count   
                
def game(count):
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
    print(f"You won {player_score} out of {count} times")
    again()
          
start()