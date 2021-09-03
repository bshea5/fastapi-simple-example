from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from app import schemas
from app.models import Blog
from app.database import get_db

def get_all(db: Session = Depends(get_db)):
  return db.query(Blog).all()

def create(args: schemas.Blog, db: Session = Depends(get_db)):
  new_blog = Blog(**args.dict(), user_id=1)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)

  return new_blog

def destroy(id: int, db: Session = Depends(get_db)):
  # Reminds me of cfwheels, `model("user").findOne(id = id)`
  blog = db.query(Blog).filter(Blog.id == id)

  if not blog.first(): 
    # Not sure if I'm a fan of raising this exception here, as it seems more
    # apropiate for the controller to handle
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Blog with id {id} not found")

  blog.delete(synchronize_session=False)
  db.commit()
  return f'Deleted blog with id {id}'

def update(id: int, args: schemas.Blog, db: Session = Depends(get_db)):
  blog = db.query(Blog).filter(Blog.id == id)

  if not blog.first():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f"Blog with id {id} not found")

  blog.update(args.dict())
  db.commit()

  return f'Updated blog with id {id}'

def show(id: int, db: Session = Depends(get_db)):
  blog = db.query(Blog).filter(Blog.id == id).first()

  if not blog:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail=f"Blog with the id {id} is not available."
    )

  return blog