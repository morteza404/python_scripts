import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# db_connstring = 'postgresql+psycopg2://user:password@localhost:port/dbname'

# Configuration
db_connstring = 'postgresql+psycopg2://postgres:123@localhost:5432/paravid'
engine = create_engine(db_connstring, echo = True)
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()

# Check Connection
# engine.execute('select 1').scalar()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    # CRUD : Create
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('{name}', '{fullname}', '{password}')>".format(name = self.name, 
                                                                     fullname = self.fullname,
                                                                     password = self.password)
                                                              
# print(User.__tablename__)  

# Base.metadata.create_all(engine) 

### CRUD : Create

# add_user =  User('morteza', 'arian', '123')
# add_user =  User('morteza', 'arian', '123')  
# session.add(add_user)
# session.commit()
# print(add_user.password)
# print(add_user.id)

### Create Multi user

# session.add_all([
#     User('saeed', 'salehi', '456'),
#     User('reza', 'razavi', '789')
# ])
# session.commit()
# print(session.new)

all_users = session.query(User).all()
for user in all_users:
    print(user)

### CRUD : Read

# my_user = session.query(User).filter_by(name = 'morteza').first()
# print(my_user)
# print(my_user.name)
# print(my_user.password)

### state session
# Transient
# Pending
# Persistent
# Detach
# Rollback

