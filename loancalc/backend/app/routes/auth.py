from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import SessionLocal, engine, Base
import bcrypt

# Create tables
Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup", response_model=schemas.UserResponse)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # check if user exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # hash password
    hashed_pw = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_pw.decode("utf-8")
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if not bcrypt.checkpw(user.password.encode("utf-8"), db_user.password.encode("utf-8")):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"message": "Login successful ✅", "user": {"id": db_user.id, "name": db_user.name, "email": db_user.email}}
