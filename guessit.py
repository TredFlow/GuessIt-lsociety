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
slow_print('Welcome to the game!')
time.sleep(1)
tprint('GUESS IT')
time.sleep(2)
while True:
    guess = input('Enter a number between 1 and 100:')
    attemps += 1
    if not guess.isdigit(): print("Enter the NUMBERS, bro"); continue
    i = int(guess)
    if i < 1 or i > 100: 
        slow_print('The number must be between 1 and 100!'); continue
    if i == num:
        if attemps == 1:
            slow_print(f'WTF! Are you Einstein? Even I can't guess in {attemps} attempts.')
        elif attemps <=7:
            slow_print(f'Bravo boss! {attempts} attempts, a worthy result.')
        elif attemps <=10:
            slow_print(f'More or less, {attemps} attempts, but still congratulations!')
        elif attemps >= 11:
            slow_print('Hey, dude! When did you get your IQ tested?') 
            time.sleep(1)
            slow_print('This is a cool neighborhood, get lost!') 
            time.sleep(1)
            slow_print(f'{attemps} attempts, shame!')
            time.sleep(1)
            slow_print('We're calling your mom!')
            time.sleep(1)
            tprint('BEEP')
            time.sleep(1)
            slow_print('Your mom: Are you serious? I'll give him up right now.')
            time.sleep(1)
            tprint('HAHAHAHA')
            time.sleep(1)
            tprint('DONT CRY')

        break
    elif i < num:
        slow_print('The number is higher!')
    elif i > num:
        slow_print('The number is less!')

    
    
    


