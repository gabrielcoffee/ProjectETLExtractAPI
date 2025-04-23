from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String, Integer, DateTime
from datetime import datetime

# Cria a classe Base do SQLAlchemy (na versão 2.x)
Base = declarative_base()

class BitcoinPreco(Base):
    """Define a tabela no banco de dados."""
    __tablename__ = 'coinbase_banco'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    criptocurrency = Column(String(50), nullable=False)
    currency = Column(String(10), nullable=False)
    timestamp = Column(DateTime, default=datetime.now())