import time
import requests
from tinydb import TinyDB
from datetime import datetime

def extract():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    data = response.json()
    return data

def transform_cripto_data(data):
    data = data['data']
    value = data['amount']
    criptocurrency = data['base']
    currency = data['currency']
    timestamp = datetime.now().timestamp()

    transformed_data = {
        'value': value,
        'criptocurrency': criptocurrency,
        'currency': currency,
        'timestamp': timestamp
    }

    return transformed_data

def save_data_tinydb(data, db_name="bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(data)
    print("Dados salvos com sucesso!")

if __name__ == '__main__':
    while True:
        data = extract()
        transformed_data = transform_cripto_data(data)
        save_data_tinydb(transformed_data)
        time.sleep(15)