from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    signup_date: str
    signup_month: int
    signup_year: int
    interests: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    signup_date: Optional[str] = None
    signup_month: Optional[int] = None
    signup_year: Optional[int] = None
    interests: Optional[str] = None

class User(UserBase):
    email: str

    class Config:
        orm_mode = True
