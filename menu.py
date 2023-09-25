import main
import os

def menu():
    while True:
        os.system('cls')
        print('TES KORAN')
        inp = input('> ')
        if inp == '10':
            break
        else:
            main.play()

        