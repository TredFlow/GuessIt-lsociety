import random
import time
from modguess import slow_print, messages, tprint
from guessrecord import record_check, record_guess
from languess import Translations
lang = input("Choose language / Выбери язык (en/ru): ").lower()
if lang not in ['ru', 'en']: 
    lang = 'en' 
best_score = record_check()
num = random.randint(1, 100)
attempts = 0
slow_print(Translations [lang]['start'])
time.sleep(1)
tprint('GUESS IT')
time.sleep(2)
slow_print(Translations [lang]['record_status'].format(best_score))
time.sleep(1)
while True:
    guess = input(Translations [lang]['guess'])
    attempts += 1
    if not guess.isdigit(): 
        print(Translations [lang]['numbers_only'])
        continue
    i = int(guess)
    if i < 1 or i > 100: 
        slow_print(Translations [lang]['range'])
        continue
    if i == num:
        messages(attempts, lang)
        break
    elif i < num:
        slow_print(Translations [lang]['higher'])
    elif i > num:
        slow_print(Translations [lang]['less'])

record_guess(attempts, best_score, lang)

Exit = input(Translations [lang]['exit'])









