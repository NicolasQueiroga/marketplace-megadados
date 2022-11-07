import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database


SERVER_USERNAME = os.getenv("SERVER_USERNAME")
SERVER_PASSWORD = os.getenv("SERVER_PASSWORD")
SERVER_NAME = os.getenv("SERVER_NAME")
SERVER_DB = os.getenv("SERVER_DB")

SQLALCHEMY_DATABASE_URL = f"mysql://{SERVER_USERNAME}:{SERVER_PASSWORD}@{SERVER_NAME}/{SERVER_DB}"

if not database_exists(SQLALCHEMY_DATABASE_URL):
    create_database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False, 
    autoflush=False 
    )

Base = declarative_base()