from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from app.database import get_db
from app import schemas, oauth2
from app.services import users

router = APIRouter(
  prefix="/users",
  tags=["users"],
  # lock it down!
  # dependencies=[Depends(oauth2.get_current_user)],
  responses={}
)

@router.post('', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create(request: schemas.User, db: Session = Depends(get_db)):
  return users.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def show(id: int, db: Session = Depends(get_db)):
  return users.show(id, db)