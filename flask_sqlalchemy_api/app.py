from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields

app = Flask(__name__)
# app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"({self.username}, {self.email})"

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("username", "email")

user_schema = UserSchema()
users_schema = UserSchema(many = True)


@app.route("/")
def home():
    return "salam"

# endpoint to create new user
@app.route("/user", methods = ["POST"])
def add():
    username = request.json["username"]
    email = request.json["email"]
    user = User(username, email)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)

# endpoint to show all users
@app.route("/user", methods = ["GET"])
def get_all():
    users = User.query.all()
    return users_schema.jsonify(users)

# endpoint to get user detail by id
@app.route("/user/<int:id>", methods = ["GET"])
def get_one(id):    
    user = User.query.get(id)
    return user_schema.jsonify(user)

# endpoint to update user
@app.route("/user/<id>", methods = ["PUT"])
def update(id):
    user = User.query.get(id)
    username = request.json["username"]
    email = request.json["email"]
    user.username = username
    user.email = email
    db.session.commit()
    return user_schema.jsonify(user)

# endpoint to delete user
@app.route("/user/<id>", methods = ["DELETE"])
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000 , debug=True)