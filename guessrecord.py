import os
from art import tprint
from languess import Translations
def record_check():
    file_name = 'record.txt'
    if  not os.path.exists(file_name ):
        with open ('record.txt', 'w') as f:
          f.write(str(100))
        return(100)
    with open(file_name, 'r') as f:
        content = f.read().strip()
        return int(content) if content else 100
    
def record_mod(new_record):
    with open ('record.txt', 'w') as f:
       f.write(str(new_record))

def record_guess(attempts, current_record, lang):
    attempts = int(attempts)
    current_record = int(current_record)
    if attempts == current_record:
        print(Translations [lang]['quote'])
        tprint(Translations [lang]['look'])
    elif attempts < current_record:
        print(Translations [lang]['new_record'].format(current_record - attempts))
        record_mod
    elif attempts > current_record:
        print(Translations [lang]['bad_record'].format(attempts))
        
