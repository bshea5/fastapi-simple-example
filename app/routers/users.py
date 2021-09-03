from app.database import get_session
from app.models.User import User
from fastapi import APIRouter, Depends, status
from app import schemas, oauth2
from app.services import users
from sqlmodel import Session
from app.hashing import Hash

router = APIRouter(
  prefix="/users",
  tags=["users"],
  # lock it down!
  # dependencies=[Depends(oauth2.get_current_user)],
  responses={}
)

@router.post('', response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def create_hero(*, session: Session = Depends(get_session), args: schemas.UserCreate):
    args.password = Hash.encrypt(args.password)
    db_user = User.from_orm(args)
    # session.add(db_user)
    # session.commit()
    # session.refresh(db_user)
    # return db_user

    return users.create(db_user, session)

@router.get('/{id}', response_model=schemas.UserRead, status_code=status.HTTP_200_OK)
def show(*, session: Session = Depends(get_session), id: int):
  user = session.get(User, id)
  return user
