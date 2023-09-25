import random
import os
import time
import menu

def play():
    inp = ''
    gameCounter = 0
    scoreCounter = 0
    startTime = time.time()
    while inp != '10':
        os.system('cls')
        a = random.randrange(0,9)
        b = random.randrange(0,9)
        print(a)
        print(b)
        string = str(a+b)
        ans = string[-1]

        inp = input('> ')
        endTime = int(time.time() - startTime)
        gameCounter += 1
        if inp == ans:
            scoreCounter += 1
        if endTime >= 60:
            break
    salahCount = gameCounter - scoreCounter
    ansSpeed = gameCounter/60
    os.system('cls')
    print(f'Pertanyaan Dijawab: {gameCounter}\nSkor: {scoreCounter}\nSalah: {salahCount}\nKecepatan Menjawab: {ansSpeed} soal/detik')
    input('> ')
    menu.menu()
    