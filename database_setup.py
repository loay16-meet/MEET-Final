from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'Profiles'
    name = Column(String)
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    group = Column(Integer)


class Group(Base):
    __tablename__ = 'Groups'
    name = Column(String)
    id = Column(Integer, primary_key=True)
    users_id= Column(Integer)
    desc = Column(String)
    pic = Column(Integer)
    
    

