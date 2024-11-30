# import the module's function that needed
from random import randrange

def randnumber():
    '''Create the goal number that players need to guess'''
    rand_num = randrange(1,101)
    return rand_num

def guessnum():
    '''Ensure the number entered is an integer between 1 and 100'''
    while True:
        try:
            guess_num = int(input('Guess a number between 1 and 100, if you want to stop playing, enter 0 '))
            if guess_num >= 0 and guess_num <= 100: # Include 0 as a sentinal for stopping the game
                return guess_num
        except ValueError:
            print('This value is invalid, please enter a number between 1 and 100')
            guess_num = int(input('Guess a number between 1 and 100: '))

def level(level_now):
    while True:
        if level_now==1:
            return 10
        if level_now==2:
            return 7
        if level_now==3:
            return 5


def gameplay():
    '''Main logic of game play'''
    random_num = randnumber()
    times = 0
    while True:
        guess_num = guessnum()
        if guess_num == 0:
            print("Thank you for playing!, see you next time!")
            break
        times += 1
        if guess_num == random_num:
            print('Congrats! You guessed the correct number!, Thank you for playing!')
            break

        if guess_num > random_num:
            print('Opps, you\'re wrong, guess a smaller number!')
        if guess_num < random_num:
            print('Opps, you\'re wrong, guess a larger number!')
        if times >10:
            print("Sorry! You lose")
            break



def main():
    '''Ask players to decide to play again or not'''
    gameplay()
    while True:
        response = input('Would you like to play again? (y/n): ').lower().strip()
        if response == 'y':
            gameplay()
        else:
            print('Thank you for playing!')
            break
if __name__ == '__main__':
    main()







