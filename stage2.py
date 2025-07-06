#number guessing game-Python
import random

lowest_num = 1
highest_num = 50
guesses = 0
answer = random.randint(lowest_num,highest_num)
is_running = True

print('Welcome to the Python Number-Guessing Game')
print(f"Please select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input('Enter your Number:')
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print('Out of range')
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess > answer:
            print('Too high')
        elif guess < answer:
            print('Too low')
        else:
            print('Correct Answer!')
            print(f'{guess} is the correct answer')
            print(f'You have guessed in {guesses} guesses')
            is_running = False
    else:
        print('Invalid Input')
        print(f"Please select a number between {lowest_num} and {highest_num}")


