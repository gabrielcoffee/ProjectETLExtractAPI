import os
import time
import requests
import logging
import logfire
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from logging import basicConfig, getLogger

# Configuração Logfire
logfire.configure()
basicConfig(handlers=[logfire.LogfireLoggingHandler()])
logger = getLogger(__name__)
logger.setLevel(logging.INFO)
logfire.instrument_requests()
logfire.instrument_sqlalchemy()

# table model
from database import Base, BitcoinPreco

load_dotenv()
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# cria sessao e engine
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# cria tabela
def create_table():
    Base.metadata.create_all(bind=engine)
    logger.info("Tabela criada com sucesso!")

def extract_bitcoin_data():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    data = response.json()
    return data

def transform_cripto_data(data):
    data = data['data']
    value = data['amount']
    criptocurrency = data['base']
    currency = data['currency']
    timestamp = datetime.now()

    transformed_data = {
        'value': value,
        'criptocurrency': criptocurrency,
        'currency': currency,
        'timestamp': timestamp
    }

    return transformed_data

def save_data_postgres(data):
    session = Session()
    bitcoin_preco = BitcoinPreco(**data)
    session.add(bitcoin_preco)
    session.commit()
    session.close()

if __name__ == '__main__':
    create_table()


    while True:
        try:
            json_data = extract_bitcoin_data()
            if json_data:
                transformed_data = transform_cripto_data(json_data)
                logger.info("Dados tratados com sucesso!")

                save_data_postgres(transformed_data)
                logger.info("Dados salvos com sucesso!")
        except Exception as e:
            logger.info(f"Erro: {e}")
        time.sleep(15)
