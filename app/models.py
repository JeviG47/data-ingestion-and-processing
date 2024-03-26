from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"

    email = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    signup_date = Column(String)
    signup_month = Column(Integer)
    signup_year = Column(Integer)
    interests = Column(String)
