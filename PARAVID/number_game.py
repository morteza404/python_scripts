# limit the number of gueses
# catch when someone submits a non-integer value
# print 'too high' or 'too low' for bad guesses
# let player play again

import random

# generate a random number between 1 to 10
secret_number = random.randint(1, 10)

def run_game():

    guesses = []
    guess = 0
    
    while len(guesses) < 5:
        # safely make an int
        try:
            # get a number guess from the player
            guess = int(input('Guess a number between 1 to 10 : '))
        except ValueError:
            print('{} is not a number!'.format(guess))

        else:
            # compare guess the secret number
            if guess == secret_number:
                print('you got it! number was {}'.format(secret_number))
                break
            elif guess < secret_number:
                print('number is higher than {}'.format(guess))
            elif guess > secret_number:
                print('number is lower than {}'.format(guess))
            else:
                # print hit/miss
                print('that is not it!')
        guesses.append(guess)
    else:
        print('you did not get it. number was {} .'.format(secret_number))
    play_again = input('do you want play again?[Y/N] ')
    if play_again.lower() != 'n':
        run_game()
    else:
        print('Bye!')

run_game()

       



