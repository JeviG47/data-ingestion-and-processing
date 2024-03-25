from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create User
@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db=db, user=user)

# Get User by Email
@router.get("/users/{email}", response_model=schemas.User)
def read_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Update User by Email
@router.put("/users/{email}", response_model=schemas.User)
def update_user(email: str, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db=db, email=email, user_data=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Delete User by Email
@router.delete("/users/{email}")
def delete_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# Fetch users who signed up in the last month and have a specific interest
@router.get("/users/last-month-with-interest/")
def get_users_last_month_with_interest(interest: str, db: Session = Depends(get_db)):
    query = """
        SELECT *
        FROM users
        WHERE signup_date >= DATEADD(month, DATEDIFF(month, 0, GETDATE()) - 1, 0)
          AND signup_date < DATEADD(month, DATEDIFF(month, 0, GETDATE()), 0)
          AND interests LIKE ?
        ORDER BY signup_date;
    """
    users = db.execute(query, (f'%{interest}%',)).fetchall()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

