from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your connection parameters
DATABASE_URL = "mssql+pyodbc://adm:Waterford120@onetwenty-user-srv.database.windows.net:1433/user-db?driver=ODBC+Driver+17+for+SQL+Server"

# Create the engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": "require"},
    echo=True  # Set to True to see SQL queries being executed
)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a base for declarative class definitions
Base = declarative_base()
