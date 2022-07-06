from os import system
from random import randint, choice
from time import sleep
import pyfiglet

score = 0
def game(randlist):
    system('clear')
    for i in randlist:
        print('\t\t\t\n\n\n\n')
        print(pyfiglet.figlet_format(f'{i}', font='banner3-D'), end=' ')
        input('if you see enter to next number: ')
        system('clear')
    lostnumber = choice(randlist)
    randlist.remove(lostnumber)
    print(randlist)
    if int(input('who number is lost: ')) == lostnumber:
        global score
        score += 10
        print('good job!')
        print('your score is: ', score)
        if input('Would you play (y/n): ') == 'n':
            exit(0)
        else:
            level = input('If you like change level please insert h: hard or m: mediom or e: easy and you dont just press enter')
            main(level)
    else:
        print('fuck.bitch, I mussed up excuse me man. ')
        if input('Do you wanna play?(yes\\n): ') == 'n':
            exit(0)
        else:
            level = input('If you like change level please insert h: hard or m: mediom or e: easy and you dont just press enter')
            main(level)





def main(level):
    system('clear')
    print(level)
    if level == 'q':
        n = input('game level(hard(h), mediom(m), easy(e)): ')
    else:
        n = level
    if n == 'h':
        n = 15
        numberrange = 100
    elif n == 'm':
        n = 10
        numberrange = 50
    else:
        n = 5
        numberrange = 10
    randlist = [randint(1, numberrange) for _ in range(n)]
    game(randlist)

if __name__ == '__main__':
    main('q')
