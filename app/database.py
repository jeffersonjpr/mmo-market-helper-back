from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import Base

engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
