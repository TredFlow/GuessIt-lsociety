import random
import time
from modguess import slow_print, messages, tprint, level_status
from guessrecord import record_check, record_guess
from languess import Translations
lang = input("Choose language / Выбери язык (en/ru/uk/jp): ").lower()
if lang not in ['ru', 'en', 'uk', 'jp']:
    lang = 'en' 
name = input(Translations [lang]['name'])
best_score = record_check()
attempts = 0
slow_print(Translations [lang]['start'].format(name))
time.sleep(1)
tprint('GUESS IT')
time.sleep(1)
slow_print(Translations [lang]['record_status'].format(best_score))
slow_print(Translations [lang]['stat_clue'])
time.sleep(1)
level = input(Translations [lang]['level_status'])
max_num = level_status(level)
num = random.randint(1, max_num)
time.sleep(1)
while True:
    guess = input(Translations [lang]['guess'].format(max_num))
    if guess in ['stat']:
        print(Translations [lang]['stat_user'])
        with open ('record.txt','r') as f:
            print(f.read())
        continue
    attempts += 1 
    if not guess.isdigit(): 
        print(Translations [lang]['numbers_only'])
        continue
    i = int(guess)
    if i < 1 or i > max_num: 
        slow_print(Translations [lang]['range'].format(max_num))
        continue
    if i == num:
        messages(attempts, lang)
        break
    elif i < num:
        slow_print(Translations [lang]['higher'])
    elif i > num:
        slow_print(Translations [lang]['less'])

record_guess(name, attempts, best_score, lang)

Exit = input(Translations [lang]['exit'])
    









