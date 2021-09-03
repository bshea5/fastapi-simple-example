from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Path to file to use as database source
SQLALCHEMY_DATABASE_URL ='sqlite:///./database.db'
args = {
  "check_same_thread": False
}

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

def generate_missing_tables():
  Base.metadata.create_all(engine)