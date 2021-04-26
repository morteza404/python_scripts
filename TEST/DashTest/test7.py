import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

# df = pd.read_csv('nodes.csv')

header_names =[ 'source', 'target']
df = pd.read_csv('force2.csv',names=header_names)


app.layout = html.Div([
    dcc.Graph(
        id='Iris Viz',
        figure={
            'data': [
                go.Scatter(
                    # x=df[df['species'] == i]['petal_length'],
                    # y=df[df['species'] == i]['sepal_length'],
                    x=df['source'],
                    y=df['target'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    line={
                        'dash' : 'solid'
                    }
                ) 
            ],
            'layout': go.Layout(
                xaxis={'title': 'source'},
                yaxis={'title': 'target'},
                margin={'l': 200, 'b': 40, 't': 100, 'r': 200},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()
