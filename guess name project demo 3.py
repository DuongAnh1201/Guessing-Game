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
            attempts= 10
            level_now +=1
            return attempts
        if level_now==2:
            attempts= 7
            level_now +=1
            return attempts
        if level_now==3:
            attempts= 5
            return attempts


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
    return times


def result():
    level_now = 1
    total_points = 0
    while level_now <= 3:
        attempts = level(level_now)
        times = gameplay()

        if times is None:  # Game was stopped
            break

        if times > attempts:
            print("Sorry, You lose!")
            break

        attempts_left = attempts - times
        if level_now == 1:
            total_points += attempts_left * 10
        elif level_now == 2:
            total_points += attempts_left * 15
        elif level_now == 3:
            total_points += attempts_left * 20

        level_now += 1

    print(f"You finished the game! You earned a total of {total_points} points.")
    return total_points

def main():
    '''Ask players to decide to play again or not'''
    display_result = result()
    while True:
        print(f"You got {points_1+points_2+points_3} points in total")
        response = input('Would you like to play again? (y/n): ').lower().strip()
        if response == 'y':
            gameplay()
        else:
            print('Thank you for playing!')
            break
if __name__ == '__main__':
    main()







