from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///urls.db", echo=False)
SessionLocal = sessionmaker(bind=engine)
