import json

from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer,primary_key=True)
    title = Column(String)
