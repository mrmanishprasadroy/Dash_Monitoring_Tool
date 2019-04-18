import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import json
from app import app
import pandas as pd

layout = html.Div([
    dcc.Dropdown(
        id='measurment-dropdown',
        options=[
            {'label': '{}'.format(i), 'value': i} for i in [
                'Thickness 1', 'Length 1', 'StripSpeed 1', 'GcsActive G1', 'GcsActive G2', 'GcsActive G3',
                'GcsActive G4', 'GcsActive G5', 'FcsActive G1', 'FcsActive G2', 'FcsActive G3', 'FcsActive G4',
                'FcsActive G5'
            ]
        ],
        multi=True,
        value=['GcsActive G1', 'GcsActive G2', 'GcsActive G3', 'GcsActive G4', 'GcsActive G5']
    ),
    # Chart Container
    html.Div(
        [
            dcc.Graph(
                id="meas_plot",
                config=dict(displayModeBar=False),
            ),
        ], className="sms_chart_div", style={"marginBottom": "10"}
    )
])


@app.callback(
    Output('meas_plot', 'figure'),
    [Input('measurment-dropdown', 'value'), Input('meas_dataset_df', 'children')])
def display_value(selected_value, dataset):
    data = json.loads(dataset)
    df_bigdata = pd.read_json(data['df_01'], orient='split')
    df_bigdata = df_bigdata.reset_index()
    trace0 = []
    for item in selected_value:
        # Create and style traces
        trace0.append(go.Scatter(
            x=df_bigdata['index'],
            y=df_bigdata[item],
            name=item,
            line=dict(
                # color=('rgb(205, 12, 24)'),
                # dash='dash',
                width=4)
        ))

    traces = [trace0]
    data = [val for sublist in traces for val in sublist]

    # Edit the layout
    layout = dict(title='measurement points "{}"'.format(selected_value),
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
