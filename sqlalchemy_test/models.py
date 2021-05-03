from sqlalchemy import Column, Integer, String

class User:
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User({self.username})"