pip3 install -r requirements.txt

https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

1.enter into python interactive shell
First you need to enter into python interactive shell using following command in your terminal:
$ python

2. import db object and generate SQLite database
Use following code in python interactive shell
>>> from app import db
>>> db.create_all()
And crud.sqlite will be generated inside your flask_tutorial folder.

3. Run flask application
Now after generate sqlite database, we are ready to run our flask application. Run following command from your terminal to run your application.
$ python app.py