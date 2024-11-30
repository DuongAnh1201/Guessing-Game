from random import randrange
def randnum():
    ''' Generate a random number '''
    rand_num = randrange(1,101)
    return rand_num

def guessnum():
    '''receiving input data'''
    while True:
        try:
            guess_num = int(input('Guess a number between 1 and 99, if you want to stop, enter 0: '))
            if 0<=guess_num <100:
                return guess_num
        except ValueError:
            print("Something went wrong, please guess a number between 1 and 99")
            guessnum()


def gameplay():
    '''Main game loop'''
    rand_num = randnum()
    count= {}
    level=1
    times=0
    while True:
        guess_num = guessnum()
        times=times+1
        #Response for each specified situation
        if guess_num==0:
            print("Thank you for playing!")
            break
        if rand_num > guess_num:
            print("You\'re wrong, guess a higher number!")
        if rand_num < guess_num:
            print("You\'re wrong, guess a lower number!")
        if rand_num == guess_num:
            if level == 1:
                count["level1"]= times
            if level == 2:
                count["level2"]= times
            if level == 3:
                count["level3"]= times
                print("You finished this game")
                break
            print("Congrats! You guessed the number!, let's move to the next level")
            rand_num = randnum()
            level+=1
    return count

def result():
    # Count for the result
    count=gameplay()
    count['level2']=count['level2']-count['level1']
    count['level3']=count['level3']-count['level2']-count['level1']
    if count['level1']<10 and count['level2']<7 and count['level3']<7:
        point=50*count['level1'] + 50*count['level2'] + 50*count['level3']
        return point
    if count['level1']<10 and count['level2']<7 and count['level3']<5:
        point=50*count['level1'] + 50*count['level2']+70*count['level3']
        return point
    else:
        point=50*count['level1'] + 35*count['level2']+25*count['level3']
        return point
def main():
    #direct the response and main game play, also memory the result

    while True:
        resp = input(
            "What would you like to do?\n1. Play again\n2. Stop\n3. Show High rank\n4. Delete the rank\n").strip().lower()
        if resp == '1':
            point = result()
            print("Thank you for playing!")
            name = input('Enter your name:')
            with open("test.txt", "a+") as f:
                dict_result = {}
                dict_result[name] = point
                f.write('name' + '                                  ' "point")
                f.write("\n")
                for keys, values in dict_result.items():
                    f.write(f"{keys:<38}{values}\n")
        if resp == '2':
            print("Thanks for playing!")
            break
        if resp == '3':
            with open("test.txt", "r") as f:
                print(f.read())
        if resp == '4':
            with open("test.txt", "w") as f:
                f.write('name' + '                                  ' "point")

if __name__ == '__main__':
    main()













