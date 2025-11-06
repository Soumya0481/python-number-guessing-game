import random
target=random.randint(1, 100)
print("Welcome to 'Guess the Number'Gameeeeee!")
attempts = 10
while attempts > 0:
    userguess =input("guess the target number or quit the game Q:\n ")
    if userguess == 'Q' or userguess == 'q':
        print("Thanks for playing! Goodbye.")
        break
    guess = int(userguess)
    attempts -= 1
    if guess < target:
        print("your guess number is too small ! think bigger\n")
    elif guess > target:
        print("your guess number is to high !think smaller\n")
    else:
        print("Congratulations! You've guessed the number!\n\n")
        break
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {target}\n\n.")
    else:
        print(f"You have {attempts} attempts left.\n")
 
print("Game Over.\n")
