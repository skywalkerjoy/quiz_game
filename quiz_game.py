print("Welcome to my laptop")

answer = input("Would you like to play a game? ").lower()
if answer != 'yes':
    quit()
else:
    print('Okay,lets start!')
score = 0
answer = input("what is your favourite number? ")
if answer == '1':
    print('Correct!')
    score = score+1
else:
    print('Incorrect')

answer = input("what is your school name? ").lower()
if answer == 'sinclair':
    print('Correct!')
    score=score+1
else:
    print('Incorrect')

print('You got '+ str(score)+ ' questions correct')

