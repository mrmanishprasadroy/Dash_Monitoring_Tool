import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import json
from app import app
import pandas as pd

layout = html.Div([
    dcc.Dropdown(
        id='exitarea-dropdown',
        options=[
            {'label': '{}'.format(i), 'value': i} for i in [
                'strip_length_1', 'strip_length_2', 'coiler_in_use'
            ]
        ],
        multi=True,
        value=['strip_length_1', 'strip_length_2']
    ),
    # Chart Container
    html.Div(
        [
            dcc.Graph(
                id="exit_plot",
                config=dict(displayModeBar=False),
            ),
        ], className="row", style={"marginBottom": "10"}
    ),

    # Chart Container
    html.Div(
        [
            dcc.Graph(
                id="coilid_plot",
                config=dict(displayModeBar=False),
            ),
        ], className="row", style={"marginBottom": "10"}
    )
])


@app.callback(
    Output('exit_plot', 'figure'),
    [Input('exitarea-dropdown', 'value'), Input('coiler_dataset_df', 'children')])
def display_value(selected_value, dataset):
    data = json.loads(dataset)
    df_bigdata = pd.read_json(data['df_01'], orient='split')
    # df_bigdata = df_bigdata.reset_index()
    df_bigdata = df_bigdata.sort_values('timeIndex')
    trace0 = []
    for item in selected_value:
        # Create and style traces
        trace0.append(go.Scatter(
            x=df_bigdata['timeIndex'],
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
    layout = dict(title='Exit Area "{}"'.format(selected_value),
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


@app.callback(
    Output('coilid_plot', 'figure'),
    [Input('exitarea-dropdown', 'value'), Input('coiler_dataset_df', 'children')])
def display_coil_value(selected_value, dataset):
    data = json.loads(dataset)
    df_bigdata = pd.read_json(data['df_01'], orient='split')
    # df_bigdata = df_bigdata.reset_index()
    df_bigdata = df_bigdata.sort_values('timeIndex')
    index = df_bigdata['timeIndex']
    coil_1 = df_bigdata['coil_id_out_1']
    coil_2 = df_bigdata['coil_id_out_2']
    # Create and style traces
    trace0 = go.Scatter(
        x=index,
        y=coil_1,
        name='Coiler 1',
        text=coil_1,
        line=dict(
            # color=('rgb(205, 12, 24)'),
            dash='dash',
            width=4)
    )

    # Create and style traces
    trace1 = go.Scatter(
        x=index,
        y=coil_2,
        name='Coiler 2',
        text=coil_2,
        line=dict(
            # color=('rgb(205, 12, 24)'),
            # dash='dash',
            width=4)
    )

    data = [trace0, trace1]

    # Edit the layout
    Layout = dict(title='coil id out',
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
    fig = dict(data=data, layout=Layout)
    return fig
