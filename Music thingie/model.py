from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()

class Feedback(Base):
	__tablename__ = 'Feedback'
	id = Column(Integer , primary_key=True)
	feedback = Column(String)
	playlist = Column()

	def __repr__(self):
		return ("Playlist: {} \nFeedback: {}").format(self.playlist , self.feedback)