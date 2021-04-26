from flask import Flask
from math import *

app = Flask(__name__)

@app.route('/users/<username>')
def profile(username):
    return 'welcome to the profile of ' + username

@app.route('/math/<number>')
def power(number):
    return 'the sqrt of number is: {}'.format(sqrt(int(number)))   

if __name__ == '__main__':
    app.run(debug=True)