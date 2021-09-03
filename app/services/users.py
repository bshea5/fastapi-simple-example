from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from app import schemas
from app.models import User
from app.database import get_db
from app.hashing import Hash

def create(args: schemas.User, db: Session = Depends(get_db)):
  args.password = Hash.encrypt(args.password)
  user = User(**args.dict())
  # user = User(name=args.name, email=args.email, password=args.password)
  db.add(user)
  db.commit()
  db.refresh(user)
  return user

def show(id: int, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == id).first()
  if not user:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail=f"User with the id {id} is not available."
    )

  return user