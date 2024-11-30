from distutils.command.clean import clean
from random import randrange

def randnum():
    #generalizing the number that players need guess
    rand_num = randrange(1,100)
    return rand_num

def guessnum():
    #typing the number that player guess
    guess_num = int(input('Enter a number between 1 and 100, if you wanna stop game, press 0: '))
    while True:
        if guess_num < 0 or guess_num > 100:
            guess_num=int(input('Enter a number between 1 and 100, if you wanna stop game, press 0: '))
        return guess_num


def gameplay():
    random_num = randnum()
    number_level = 1
    times = 0
    dict={}
    while True:
        guess_num = guessnum()
        times = times + 1
        if guess_num == 0:
            print("Thanks for playing!")
            break
        if guess_num> random_num:
            print('Opps, you\'re wrong, guess a smaller number!')
        if guess_num < random_num:
            print('Opps, you\'re wrong, guess a larger number!')
        if guess_num == random_num:
            print("Congrats! That's a correct answer")
            print("Let's move to the next level")
            if number_level == 1:
                dict["number_level1"]= times
            if number_level == 2:
                dict["number_level2"]= times
            if number_level == 3:
                dict["number_level3"]= times
                break
            number_level = number_level + 1
            random_num = randnum()
    return dict

def main():
    with open("ranktable.rtf", "r+") as f:
        dict= gameplay()
        result = {}
        while True:
            dict["number_level2"]=dict["number_level2"]-dict["number_level1"]
            dict["number_level3"]=dict["number_level3"]-dict["number_level2"]
            '''
            Counting point and sorting high ranking
            '''
            if dict["number_level1"] < dict["number_level2"]<dict["number_level3"]:
                point=dict["number_level1"]*50 + dict["number_level2"]*25+dict["number_level3"]*10
            elif dict["number_level2"] < dict["number_level1"]<dict["number_level3"]:
                point=dict["number_level1"]*25 + dict["number_level2"]*50+dict["number_level3"]*10
            else:
                point=dict["number_level2"]*50 + dict["number_level3"]*25+dict["number_level1"]*100
            name= input("Enter your name: ")
            result[name]=point
            sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

            resp=input("What would you like to do?\n1. Play again\n2. Stop\n3. Show High rank\n4. Delete the rank").strip().lower()
            if resp=='1':
                dict=gameplay()
            if resp=='2':
                print("Thanks for playing!")
                break
            if resp=='3':
                f.write(f"{name:<50}{point}")
                for x, y in sorted_result:
                    f.write(f'{x:<50}{y}')
                print(f.read())
            if resp=='4':
                del result



if __name__ == '__main__':
    main()



















