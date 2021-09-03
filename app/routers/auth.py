from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app import schemas
from app.hashing import Hash
from app import token 
from app.models import User
from sqlmodel import Session, select
from app.database import get_session

router = APIRouter(
  tags=['authentication']
)

@router.post('/login', response_model=schemas.Token)
def login(*, session: Session = Depends(get_session), request: OAuth2PasswordRequestForm = Depends()):
  user = session.exec(select(User).where(User.email == request.username)).one()

  if not user or not Hash.verify(request.password, user.password):
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail="Invalid Credentials"
    )

  access_token = token.create_access_token(data={"sub": user.email})

  return {"access_token": access_token, "token_type": "bearer"}
