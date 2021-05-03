from sqlalchemy import column, engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy import Column, Integer, String


conn_str = "sqlite:///test.db"
engine = create_engine(conn_str)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User({self.username})"

def create():
    Base.metadata.create_all(engine)

def add(user):
    session.add(user)
    session.commit()
    print("added")

def get():
    return session.query(User).all()

if __name__ == "__main__":
    user = User("ali",456)
    # add(user)
    print(get())

