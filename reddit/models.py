from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database setting from settings.py.
    Returns sqlalchemy engine instance
    """

    return create_engine(get_project_settings().get('CONNECTION_STRING'))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class RedditDB(DeclarativeBase):
    __tablename__ = 'reddit_table'

    id = Column(Integer, primary_key=True)
    title = Column('title', String(50))
    subreddit = Column('subreddit', String(50))
    comment_num = Column('comment_num', String(50))
    upvotes = Column('upvotes', String(50))
