from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('dtest.csv')
    # person_name = 'AsiaNet'
    # return render_template('index.html', pname = person_name)
    return df.to_html()

if __name__ == '__main__':
    app.run(debug=True)    
