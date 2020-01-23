from model import Base, Feedback

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_feedback(playlist, feedback):
	feed_object = Company(playlist = companyName , feedback = feedback)
	session.add(feed_object)
	session.commit()

def get_feedback(playlist):
	feed = session.query(Feedback).filter_by(playlist = playlist).first()
	return feed