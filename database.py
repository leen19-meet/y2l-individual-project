from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()
def function(parameter):
    pass

def get_all_users():
    users = session.query(Add_story).all()
    return users 

def find_story_by_id(id):
    story = session.query(Story).filter_by(id=id).first()
    return story

def add_story(content, picture, spouse1, spouse2, title):
    new_story = Story()
    new_story.title = title
    new_story.content= content
    new_story.picture= picture
    new_story.spouse1=spouse1
    new_story.spouse2= spouse2
    session.add(new_story)
    session.commit()

def get_all_stories():
    return session.query(Story).all() 