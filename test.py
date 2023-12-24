import random
import time
import pyautogui as pg 

def rand():
    rand = random.randint(1, 3)
    return rand

def main():
    while True:
        time.sleep(2)
        if rand() == 1:
            pg.press('a')
        elif rand() == 2:
            pg.press('d')
        elif rand() == 3:
            pg.press('s')

if __name__ == '__main__':
    main()