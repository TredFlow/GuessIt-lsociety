import requests

FORM_URL_RECORD = "https://docs.google.com/forms/d/e/1FAIpQLSebD-x46-rfEkcfLgCBbdvsbpAqfIJ-vVGviiqWWY6hreNVEw/formResponse"
ID_NAME = "entry.1334765194"
ID_ATTEMPTS = "entry.2032124735"

def send_to_record(name, attempts):
    payload = {
        ID_NAME: name, 
        ID_ATTEMPTS: attempts
    }
    try:
        requests.post(FORM_URL_RECORD, data = payload)
    except Exception as e:
        print('Ошибка! Проверьте интернет. ')
