import random

def play_the_game():
    print("WELCOME TO ROCK-PAPER-SCISSORS GAME !!")
    print("\nRules:")
    print("Rock beats Scissors.")
    print("Scissors beats Paper.")
    print("Paper beats Rocks.")
    print("\n----Let's Start The Game----")

    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        print("\nRound ",rounds + 1)
        user_choice=input("Enter your choice (rock / paper / scissors): ")
        user_choice.lower()
        choices = ["rock","paper","scissors"]
        
        if user_choice not in choices:
            print("Invalid Choice! Please Try Again.")
            continue
        
        computer_choice = random.choice(choices)
        print("Computer choice: ", computer_choice)

        if user_choice == computer_choice:
            print("Its A Tie!")
        elif(user_choice== "rock" and computer_choice=="scissors") or \
            (user_choice == "paper" and computer_choice=="rock") or \
            (user_choice== "scissors" and computer_choice=="paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!" )
            computer_score += 1

        rounds += 1
        print("Score -> You: ", user_score, " | Computer: ", computer_score)

        play_again = input("\nDo you want to play another round? (yes / no): ")
        play_again.lower()

        if play_again != "yes":
            print("\nFinal Scoreboard:")
            print("Total Rounds Played: ",rounds)
            print("Your Score: ",user_score)
            print("Computer Score: ",computer_score)

            if user_score > computer_score:
                print("Congratulations! You are the overall winner!")
            elif user_score < computer_score:
                print("Computer wins the game! Better luck next time!")
            else:
                print("It's a tie overall! ")
            print("\nThank You For Playing!")
            break

play_the_game()