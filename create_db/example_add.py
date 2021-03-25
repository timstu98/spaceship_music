from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
 
from create_database import Base, Article
 
engine = create_engine('sqlite:///../data/SSdb.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
# Insert a Person in the person table
new_person = Article(title='First one',date=datetime.datetime.now())
session.add(new_person)
session.commit()
