from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    person_name = 'AsiaNet'
    return render_template('index.html', pname = person_name)

if __name__ == '__main__':
    app.run(debug=True)    
