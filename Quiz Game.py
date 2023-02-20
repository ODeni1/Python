print('Hello guys, welcome to my quiz game!')
check = input('Do you want to play? ')

if check.lower() != 'yes':
    print("No problem, next time!")
    quit()

print("Okay, let's play!")
score = 0

answer = input("Eight o'clock in the morning is am or pm? ")
if answer.lower() == 'am':
    print('Correct!')
    score += 25
    print(f'You have {score} points')
else:
    print('Incorrect!')

answer = input('Which is the largest continents? ')
if answer.lower() == 'asia':
    print('Correct!')
    score += 25
    print(f'You have {score} points')
else:
    print('Incorrect!')

answer = input('What is the national flower in India? ')
if answer.lower() == 'lotus':
    print('Correct!')
    score += 25
    print(f'You have {score} points')

answer = input('When were the last Olympic Games held? ')
if answer.lower() == 'rio de janeiro':
    print('Correct!')
    score += 25
    print(f'You have {score} points')

print("GAME OVER")
print(f'Congratulations, you won {score} points and my respect!')