from app.models import User
from app.hashing import Hash
from sqlmodel import Session

def create(user: User, session: Session):
  user.password = Hash.encrypt(user.password)
  session.add(user)
  session.commit()
  session.refresh(user)
  return user

def show(id: int):
  with Session(engine) as session:
    user = session.get(User, id)
    return user

# def show(id: int, db: Session = Depends(get_db)):
#   user = db.query(User).filter(User.id == id).first()
#   if not user:
#     raise HTTPException(
#       status_code=status.HTTP_404_NOT_FOUND, 
#       detail=f"User with the id {id} is not available."
#     )

#   return user