import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

# Function to play the game
def play_game(user_score, computer_score):
    options = ['rock', 'paper', 'scissors']
    
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in options:
        user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    
    if result == "user":
        user_score += 1
        print("You win!")
    elif result == "computer":
        computer_score += 1
        print("You lose!")
    else:
        print("It's a tie!")

    print(f"Score: You {user_score}, Computer {computer_score}")
    return user_score, computer_score

# Main function to keep playing the game and track scores
def main():
    user_score = 0
    computer_score = 0
    play_again = 'yes'
    
    while play_again.lower() == 'yes':
        user_score, computer_score = play_game(user_score, computer_score)
        play_again = input("Do you want to play again? (yes/no): ")
    
    print(f"Final Score: You {user_score}, Computer {computer_score}")
    print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    main()
