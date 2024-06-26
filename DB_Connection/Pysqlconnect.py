from decouple import config
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import create_engine

engine = create_engine(f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_BASE')}")
base = declarative_base()

def connection(engine=engine):
    return engine