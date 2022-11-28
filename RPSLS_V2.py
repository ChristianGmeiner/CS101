import random
import sys  

choices = ["rock", "paper", "scissors", "lizard", "spock", "quit"]

class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.score = 0


    def display_results(self, message):
        print(f"{self.name} chose {self.choice} and the computer chose {computer.choice}")
        print(message)


    def win(self):
        self.score += 1
        
def display_score(player, computer):
    """ Function to display score after each turn """

    print(f"{player.name} - {player.score}    -    Computer - {computer.score}\n")    



#Main Game

print("Welcome to Rock, Paper, Scissors, Lizard, Spock\n")
player_name = input("What is your name: ").title()


# Create player objects
player = Player(player_name)
computer = Player("Computer")


# Main Game loop
while True:

    # player chooses 
    # Catches the error if user enters an invalid option and loops until valid or QUIT
    
    player_choice = input("Select your choice - Rock, Paper, Scissors, Lizard, Spock or quit the end the game ").lower()
    player.choice = player_choice
    if player_choice in choices:
        if player_choice == "quit":
            print("Goodbye")
            sys.exit(0)
    else:
        print("Please select a valid option\n")
        continue
    
                    
    # Computer chooses
    computer.choice = random.choice(choices[0:4])

    # Decides who won, displays results and increases score of wining player
    print(f"You chose {player.choice} and the computer chose {computer.choice}\n")
    if player.choice == computer.choice:
        print("It was a draw\n")
    elif player.choice == "rock" and computer.choice == "scissors":
        player.win()
        print("You won!\n")
    elif player.choice == "paper" and computer.choice == "rock":
        player.win()
        print("You won!\n")
    elif player.choice == "scissors" and computer.choice == "paper":
        player.win()
        print("You won!\n")
    elif player.choice == "lizard" and computer.choice == "spock":
        player.win()
        print("You won!\n")
    elif player.choice == "spock" and computer.choice == "scissors":
        player.win()
        print("You won!\n")
    elif player.choice == "rock" and computer.choice == "lizard":
        player.win()
        print("You won!\n")
    elif player.choice == "paper" and computer.choice == "spock":
        player.win()
        print("You won!\n")
    elif player.choice == "scissors" and computer.choice == "lizard":
        player.win()
        print("You won!\n")
    elif player.choice == "lizard" and computer.choice == "paper":
        player.win()
        print("You won!\n")
    elif player.choice == "spock" and computer.choice == "rock":
        player.win()
        print("You won!\n")
    else:
        print("You lost\n")
        computer.win()

    display_score(player, computer)