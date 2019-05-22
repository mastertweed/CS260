import random
quest = str('Enter a number between 0 and 10\n')
userinput = input(quest)
user = int(userinput)

ans = random.randrange(10)

while user != ans:
    if user < ans:
        print('Your guess is lower then the answer')
        userinput = input('Enter a number between 0 and 10\n')
        user = int(userinput)
    else:
        print('Your guess is higher then the answer')
        userinput = input('Enter a number between 0 and 10\n')
        user = int(userinput)

print('Correct')