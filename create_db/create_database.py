import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(DATE)
 
class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    artist = Column(String)
    name = Column(String)
    article_no = Column(Integer,ForeignKey('article.id'))
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///../data/SSdb.sqlite')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)