from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the engine and session
SQLALCHEMY_DATABASE_URL = "sqlite:///./links.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base model
Base = declarative_base()

# Define the link model
class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, index=True)
    short_code = Column(String, unique=True, index=True)
