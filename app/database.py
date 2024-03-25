import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve database configuration from environment variables
db_server = os.getenv("DB_SERVER")
db_name = os.getenv("DB_NAME")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")

# Define the connection string
SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc://{db_username}:{db_password}@{db_server}.database.windows.net/{db_name}?driver=ODBC+Driver+17+for+SQL+Server"

# Create database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a sessionmaker to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()
