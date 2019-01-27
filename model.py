from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Story(Base):
    __tablename__ = "stories"
    id = Column(Integer, primary_key = True)
    title=Column(String)
    content= Column(String)
    picture= Column(String)
    spouse1= Column(String) 
    spouse2= Column(String)
    # def __init__(self, title, content, picture, spouse1, spouse2):
    #     self.title = title