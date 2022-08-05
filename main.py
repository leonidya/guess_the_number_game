#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

def number_of_attempts(difficulty_level):
    """Returns number of attempts according to the choise of difficulty by the user: hard = 5, easy = 10"""
    if difficulty_level == "hard":
        attempts = 5
        return attempts
    elif difficulty_level == "easy":
        attempts = 10
        return attempts
    else:
        difficulty_level = input("Error, you didn't choose a difficulty. Type 'easy' or 'hard': ").lower()
        return number_of_attempts(difficulty_level)






def game(attempts):
    attempts_number = attempts
    computer_num = random.choice(range(1,101))
    end_of_the_game = False
    while not end_of_the_game:
        guess = int(input("Make a guess: "))
    
        if guess == computer_num:
            return print(f"You Win, the number of guesses is: {attempts_number - attempts+1}")
    
        attempts-=1
        if attempts == 0:
            return print(f"You lose, the number was: {computer_num}")
            end_of_the_game = True
        if guess > computer_num:
            print(f"To high. \nGuess again\nYou have {attempts} attemptts reamining to guess the number")
        elif guess < computer_num:
            print(f"To low. \nGuess again\nYou have {attempts} attempts reamining to guess the number")

        

from art import logo
print(logo)
print("I'm thinking of anumber between 1 and 100")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = number_of_attempts(difficulty_level)
game(attempts)









