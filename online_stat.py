import requests

FORM_URL_RECORD = "https://docs.google.com"
ID_NAME = "entry.1"
ID_ATTEMPTS = "entry.2"

def send_to_record(name, attempts):
    payload = {
        ID_NAME: name, 
        ID_ATTEMPTS: attempts
    }
    try:
        requests.post(FORM_URL_RECORD, data = payload)
    except Exception as e:
        print('Ошибка! Проверьте интернет. ')
