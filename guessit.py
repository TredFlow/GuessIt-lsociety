import random
import time
from art import tprint
import sys
def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    print()

num = random.randint(1, 100)
attemps = 0
slow_print('Добро пожаловать в игру!')
time.sleep(1)
tprint('GUESS IT')
time.sleep(2)
while True:
    guess = input('Введите число от 1 до 100:')
    attemps += 1
    if not guess.isdigit(): print("Введи ЦИФРЫ, бро"); continue
    i = int(guess)
    if i < 1 or i > 100: 
        slow_print('Число должно быть в диапазоне от 1 до 100!'); continue
    if i == num:
        if attemps == 1:
            slow_print(f'WTF! Ты че Эйнштейн? Угадать за {attemps} попытку даже мне не по зубам')
        elif attemps <=7:
            slow_print(f'Браво босс!{attemps} попыток достойный результат.')
        elif attemps <=10:
            slow_print(f'Более менее, {attemps} попыток,но все же поздравлю!')
        elif attemps >= 11:
            slow_print('Эй чудак! Ты когда на IQ проверялся?') 
            time.sleep(1)
            slow_print('Это район для крутых, проваливай!') 
            time.sleep(1)
            slow_print(f'{attemps} попыток позор!')
            time.sleep(1)
            slow_print('Звоним твоей маме!')
            time.sleep(1)
            tprint('BEEP')
            time.sleep(1)
            slow_print('Твоя мама: Да вы что серьезно? Я сейчас же откажусь от него')
            time.sleep(1)
            tprint('HAHAHAHA')
            time.sleep(1)
            tprint('DONT CRY')

        break
    elif i < num:
        slow_print('Число больше!')
    elif i > num:
        slow_print('Число меньше!')

    
    
    

