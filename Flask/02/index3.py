from flask import Flask, render_template
# import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


app = Flask(__name__)

def net():
    nodes = [1,2,3,4,5]
    links = [(1,2),(1,3),(2,4),(2,3),(4,5)]
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(links)
    nx.draw(G)
    plt.show()


@app.route('/')
def home():
    # df = pd.read_csv('dtest.csv')
    # person_name = 'AsiaNet'
    # return render_template('index.html', pname = person_name)
    # return df.to_html()
    return net().to_html()

if __name__ == '__main__':
    app.run(debug=True)    
