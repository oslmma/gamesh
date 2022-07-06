from random import randint
from os import system
from time import sleep

AREA = int(input('size of game (10: medium, 20: hard): '))
assert AREA in [10, 20]

def game():
    position_x = randint(2, AREA-3)
    position_y = randint(2, AREA-3)
    number = randint(10, 99)
    return position_x, position_y, number

def display(x, y, number):
    print(x, y, number)
    print('#' * (AREA-1))
    for i in range(AREA):
        if i != 0 or i != AREA-1:
            print('#', end='')
        for j in range(AREA):
            print(' ', end='')
            if i == x and j == y:
                print(f'\b\b{number}', end='')
        print('\b\b\b#', end='')
        print()

    print('#' * (AREA-1))

def main():
    game_level = int(input("what's game level 1, 2, 3 please give me(1: hard, 2: medium, 3: easy): "))
    assert game_level in [1, 2, 3]
    gameover = False
    score = 0
    while not gameover:
        system('clear')
        x = game()[0]
        y = game()[1]
        number = game()[2]
        display(x, y, number)
        print()
        sleep(game_level / 5)
        system('clear')
        answer = int(input('what is answer:'))
        if answer == number:
            print('that true')
            score += 10
            print(f'your score is: {score}')
            answer_user = input('Do you wanna play(yes or no)').strip().lower()
            if answer_user == 'no':
                gameover = True
        else:
            print('shit, that is incorrect')
            score -= 5 
            print(f'your score is: {score}')
            
if __name__ == '__main__':
    main()
