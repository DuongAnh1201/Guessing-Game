from random import randint, seed
def random_number():
    '''Create a random number between 1 and 100'''
    goal= randint(1,101)
    return goal

#Processing Phase
number=int(input("Guess number between 1 and 100, if you wanna stop the game, enter 0: "))
times=1
goal_number=random_number()
while number != goal_number and number!=0:
    if number > 100 or number < 1: #Make sure that player don't enter any invalid input
        print("This is invalid input, please try again, if you wanna stop the game, enter 0: ")
        number=int(input("Guess number between 1 and 100, if you wanna stop the game, enter 0: "))
    if number > goal_number:
        print(f"Opps, guess a smaller number ")
        number=int(input("Guess number between 1 and 100 if you wanna stop the game, enter 0: "))
    if number < goal_number:
        print(f"Opps, guess a larger number")
        number=int(input("Guess number between 1 and 100, if you wanna stop the game, enter 0: "))
    times = times+1 # count the numbers of times that the player guessed till they win
    if times == 5:
        if number == goal_number and number != 0:
            print("Congrats! You guessed the correct number! Let's play again!")
            number=int(input("Guess number between 1 and 100, if you wanna stop the game, enter 0: "))
            goal_number=random_number()
            times=1
        if number != goal_number and number!=0:
            print(f"Opps, you lose! Play again, guess a number between 1 and 100, if you wanna stop the game, enter 0")
            number = int(input("Guess number between 1 and 100, if you wanna stop the game, enter 0: "))
            goal_number = random_number()
            times=1
if number == 0:
    print(f"Thank you for playing this game, hope you felt well!")
if number == goal_number:
    print(f"Congratulations!!! You got {times} times to find the correct number")

