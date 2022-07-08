from random import randint

"""the function will give the player 6 attempts to guess a random number chosen by the computer.
You will receive tips at each turn (too big or too small)"""

def fortune_teller():
    print("Welcome!, Let's play\n".center(40))
    number = randint(0, 100)
    testing = 0
    while testing < 7:
        chosen = int(input('Choose a number from 0 to 100!:  '))
        testing += 1
        if chosen == number:
            print(f'Congratulations, you guessed the number from {testing} attempts')
            replay = input('Do you want to play again? Yes/No: ').upper()
            if replay == 'YES':
                fortune_teller()
            else:
                print('Goodbye!')
                break
        elif chosen > number:
            print('Ahhh..too big')
        else:
            print('Ahhh..too small')

fortune_teller()