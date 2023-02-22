import random

top_range = input('The bottom of range is 1, '
                  'please enter the top of range for this game: ')

if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print('Please enter a larger number')
else:
    print('Please enter a number next time')

random_number = random.randint(1, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess <= 0:
            print('Please enter a larger number')
    else:
        print('Please enter a number next time')

    if user_guess == random_number:
        print('You got it right!')
        break
    elif user_guess < random_number:
        print('You are below the number!')
    else:
        print('You are above the number')

print('You got it right in', guesses, 'guesses')