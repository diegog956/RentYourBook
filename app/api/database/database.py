from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError
import os

load_dotenv()

url_database = os.getenv('URL_DATABASE')

engine = create_engine(url_database)    

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except OperationalError as e:
        
        print('Base de datos no conectada.')

    finally:
        db.close()

