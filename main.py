import random

guess_number = random.randint(0,10)
guess_count = 0
guess_limit = 3
out_of_guesses = False
guess = True
while guess != guess_number and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = int(input('enter guess: '))
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")




