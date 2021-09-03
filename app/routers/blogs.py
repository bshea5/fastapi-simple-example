from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from app.database import get_db
from app import schemas, oauth2
from typing import List
from ..services import blogs

router = APIRouter(
  prefix="/blogs",
  tags=["blogs"],
  # Can enforce token checks on all routes this way, versus below where we include
  # it in the parameters, where it is accessible too.
  dependencies=[Depends(oauth2.get_current_user)],
  responses={}
)

@router.get('', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
  return blogs.get_all(db)

@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
  return blogs.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
  return blogs.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_200_OK)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
  return blogs.update(id, request, db)

@router.get('/{id}', response_model=schemas.ShowBlog, status_code=status.HTTP_200_OK)
def show(id: int, db: Session = Depends(get_db)):
  return blogs.show(id, db)