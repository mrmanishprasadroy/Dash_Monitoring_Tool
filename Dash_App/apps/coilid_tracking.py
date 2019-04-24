import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import json
from app import app
import pandas as pd

layout = html.Div([
    dcc.Dropdown(
        id='coilid-dropdown',
        options=[
            {'label': '{}'.format(i), 'value': i} for i in [
                'coil_1', 'coil_2', 'coil_3',  'coil_4', 'coil_5', 'coil_6',  'coil_7', 'coil_8',
                'coil_9', 'coil_10', 'coil_11', 'coil_12'
            ]
        ],
        multi=True,
        value=['coil_1', 'coil_2', 'coil_3',  'coil_4', 'coil_5', 'coil_6',  'coil_7', 'coil_8']
    ),
    # Chart Container
    html.Div(
        [
            dcc.Graph(
                id="coilidTracking_plot",
                config=dict(displayModeBar=False),
            ),
        ], className="row", style={"marginBottom": "10"}
    ),

])


@app.callback(
    Output('coilidTracking_plot', 'figure'),
    [Input('coilid-dropdown', 'value'), Input('coilTrack_dataset_df', 'children')])
def display_value(selected_value, dataset):
    data = json.loads(dataset)
    df_bigdata = pd.read_json(data['df_01'], orient='split')
    df_bigdata = df_bigdata.reset_index()
    index = df_bigdata['timeindex']
    trace0 = []
    for item in selected_value:
        # Create and style traces
        trace0.append(go.Scatter(
            x=index,
            y=df_bigdata[item],
            name=item,
            text=df_bigdata[item],
            line=dict(
                # color=('rgb(205, 12, 24)'),
                # dash='dash',
                width=4)
        ))

    traces = [trace0]
    data = [val for sublist in traces for val in sublist]

    # Edit the layout
    layout = dict(title='Coil ID in coil tracking',
                  xaxis={"title": "Date Time",
                         'rangeselector': {'buttons': list([
                             {'count': 1, 'label': '1M', 'step': 'minute', 'stepmode': 'backward'},
                             {'count': 10, 'label': '6M', 'step': 'minute', 'stepmode': 'backward'},
                             {'step': 'all'}
                         ])}, 'rangeslider': {'visible': True}, 'type': 'date'},
                  # yaxis=dict(title='Values'),
                  margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                  legend={'x': 0, 'y': 1},
                  hovermode='closest'
                  )
    # Plot and embed
    fig = dict(data=data, layout=layout)
    return fig
