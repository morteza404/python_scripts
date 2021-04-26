import sqlalchemy
from sqlalchemy import create_engine

db_connstring = 'sqlite:///:memory:'
engine = create_engine(db_connstring, echo = True)

engine.execute('select 1').scalar()