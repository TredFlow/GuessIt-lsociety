import os
from art import tprint
from datetime import datetime
from languess import Translations
now = datetime.now().strftime("%Y-%d-%m %H:%M")

def record_check():
    file_name = 'record.txt'
    if  not os.path.exists(file_name ):
        with open ('record.txt', 'w') as f:
          f.write('System | 100 | 1970-01-01 00:00\n')
        return 100
    with open(file_name, 'r') as f:
        lines = f.readlines()
        last_line = lines[-1].strip()
        part = last_line.split('|')
        best_score = int((part[1]).strip())
        return best_score
    return 100
    
def record_mod(name, attempts, now):
    with open ('record.txt', 'a', encoding="utf-8") as f:
        f.write(f'{name} | {attempts} | {now}\n')
    
def record_guess(name, attempts, current_record, lang):
    current_record = int(current_record)
    if attempts == current_record:
        print(Translations [lang]['quote'])
        tprint(Translations [lang]['look'])
    elif attempts < current_record:
        print(Translations [lang]['new_record'].format(current_record - attempts))
        record_mod(name, attempts, now)
    elif attempts > current_record:
        print(Translations [lang]['bad_record'].format(current_record))
        


