import json
import redis
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from telegram_definition_L1 import *
from app import app, dbc
import os
import tasks

redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])

tasks.update_segment_data()


def get_dataframe():
    """Retrieve the dataframe from Redis
    This dataframe is periodically updated through the redis task
    """
    jsonified_df = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["DATASEGMENT"]
    ).decode("utf-8")
    # df = pd.DataFrame(json.loads(jsonified_df))
    return json.loads(jsonified_df)


first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("At Stand", className="card-title"),
            dcc.Dropdown(
                id='atstand-list',
                options=[
                    {'label': '{}'.format(teltype_M21[i][0]), 'value': teltype_M21[i][0]} for i in range(0, 125)
                ],
                multi=True,
                value=[teltype_M21[0][0]]
            ),
            dcc.Graph(
                id="atstand_plot",
                config=dict(displayModeBar=False),
            ),
        ]
    )
)

second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Between  Stand", className="card-title"),
            dcc.Dropdown(
                id='betweenstand-list',
                options=[
                    {'label': '{}'.format(teltype_M22[i][0]), 'value': teltype_M22[i][0]} for i in range(0, 47)
                ],
                multi=True,
                value=[teltype_M22[0][0]]
            ),
            dcc.Graph(
                id="betweenstand_plot",
                config=dict(displayModeBar=False),
            ),
        ]
    )
)

third_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Before First Stand", className="card-title"),
            dcc.Dropdown(
                id='beforfirststand-list',
                options=[
                    {'label': '{}'.format(teltype_M23[i][0]), 'value': teltype_M23[i][0]} for i in range(0, 47)
                ],
                multi=True,
                value=[teltype_M23[0][0]]
            ),
            dcc.Graph(
                id="beforfirststand_plot",
                config=dict(displayModeBar=False),
            ),
        ]
    )
)
fourth_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("After Last Stand", className="card-title"),
            dcc.Dropdown(
                id='afterlaststand-list',
                options=[
                    {'label': '{}'.format(teltype_M24[i][0]), 'value': teltype_M24[i][0]} for i in range(0, 67)
                ],
                multi=True,
                value=[teltype_M24[0][0]]
            ),
            dcc.Graph(
                id="afterlaststand_plot",
                config=dict(displayModeBar=False),
            ),
        ]
    )
)


def serve_layout():
    return html.Div([
        dbc.Alert(id="status_pseg",color='success'),
        # Interval
        dcc.Interval(interval=30 * 1000, id="interval_pseg"),
        # Cards
        dbc.Row([dbc.Col(first_card, width=6), dbc.Col(second_card, width=6)]),
        dbc.Row([dbc.Col(third_card, width=6), dbc.Col(fourth_card, width=6)])
    ])


'''
    At stand Plotting
'''


@app.callback(
    Output('atstand_plot', 'figure'),
    [Input('atstand-list', 'value'), Input("interval_pseg", "n_intervals")])
def display_value(selected_dropdown_value, _):
    dataset = get_dataframe()
    data = json.loads(dataset)
    MP_01 = pd.read_json(data['df_01'], orient='split')
    MP_03 = pd.read_json(data['df_03'], orient='split')
    MP_05 = pd.read_json(data['df_05'], orient='split')
    MP_07 = pd.read_json(data['df_07'], orient='split')
    MP_09 = pd.read_json(data['df_09'], orient='split')
    # MP_01.to_csv('data', sep='\t', encoding='utf-8')
    # index = pd.to_datetime(MP_02['time'], format="%Y-%m-%d %H:%M:%S.%f")

    trace1 = []
    trace3 = []
    trace5 = []
    trace7 = []
    trace9 = []

    for item in selected_dropdown_value:
        # Create and style traces
        trace1.append(go.Scatter(
            x=MP_01['time'],
            y=MP_01[item],
            name=item + 'G1',
            text=MP_01[item],
            line=dict(
                # color=('rgb(22, 96, 167)'),
                dash='solid',
                width=2, )
        ))
        trace3.append(go.Scatter(
            x=MP_03['time'],
            y=MP_03[item],
            name=item + 'G2',
            text=MP_03[item],
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=2,
                dash='solid')
        ))
        trace5.append(go.Scatter(
            x=MP_05['time'],
            y=MP_05[item],
            name=item + 'G3',
            text=MP_05[item],
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=2,
                dash='solid')
        ))
        trace7.append(go.Scatter(
            x=MP_07['time'],
            y=MP_07[item],
            name=item + 'G4',
            text=MP_07[item],
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=2,
                dash='solid')
        ))
        trace9.append(go.Scatter(
            x=MP_09['time'],
            y=MP_09[item],
            name=item + 'G5',
            text=MP_09[item],
            line=dict(
                #  color=('rgb(22, 96, 167)'),
                width=2,
                dash='solid')
        ))
    traces = [trace1, trace3, trace5, trace7, trace9]
    data = [val for sublist in traces for val in sublist]

    # Edit the layout
    layout = dict(title='Process Data at stands "{}"'.format(selected_dropdown_value),
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


'''
    Between stand Plotting
'''


@app.callback(
    Output('betweenstand_plot', 'figure'),
    [Input('betweenstand-list', 'value'), Input("interval_pseg", "n_intervals")])
def display_value(selected_dropdown_value, _):
    dataset = get_dataframe()
    data = json.loads(dataset)

    MP_02 = pd.read_json(data['df_02'], orient='split')
    MP_04 = pd.read_json(data['df_04'], orient='split')
    MP_06 = pd.read_json(data['df_06'], orient='split')
    MP_08 = pd.read_json(data['df_08'], orient='split')
    # MP_01.to_csv('data', sep='\t', encoding='utf-8')
    # index = pd.to_datetime(MP_02['time'], format="%Y-%m-%d %H:%M:%S.%f")
    trace2 = []
    trace4 = []
    trace6 = []
    trace8 = []

    for item in selected_dropdown_value:
        trace2.append(go.Scatter(
            x=MP_02['time'],
            y=MP_02[item],
            name=item + ' G1-G2',
            text=MP_02[item],
            line=dict(
                # color=('rgb(205, 12, 24)'),
                width=2,
                dash='solid')  # dash options include 'dash', 'dot', and 'dashdot'
        ))
        trace4.append(go.Scatter(
            x=MP_04['time'],
            y=MP_04[item],
            name=item + ' G2-G3',
            text=MP_04[item],
            line=dict(
                # color=('rgb(205, 12, 24)'),
                width=2,
                dash='solid')
        ))
        trace6.append(go.Scatter(
            x=MP_06['time'],
            y=MP_06[item],
            name=item + ' G3-G4',
            text=MP_06[item],
            line=dict(
                #  color=('rgb(22, 96, 167)'),
                width=2,
                dash='solid')
        ))
        trace8.append(go.Scatter(
            x=MP_08['time'],
            y=MP_08[item],
            name=item + ' G4-G5',
            text=MP_08[item],
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=2,
                dash='solid')
        ))
    traces = [trace2, trace4, trace6, trace8]
    data = [val for sublist in traces for val in sublist]

    # Edit the layout
    layout = dict(title='Process Data Between stands "{}"'.format(selected_dropdown_value),
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
    Output("status_pseg", "children"),
    [Input('atstand-list', 'value'), Input("interval_pseg", "n_intervals")],
)
def update_status(value, _):
    data_last_updated = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["SEGMENT_DATE_UPDATED"]
    ).decode("utf-8")

    return "Data last updated at {}".format(data_last_updated)


'''
    Befor First stand Plotting
'''


@app.callback(
    Output('beforfirststand_plot', 'figure'),
    [Input('beforfirststand-list', 'value'), Input("interval_pseg", "n_intervals")])
def display_value(selected_dropdown_value, _):
    dataset = get_dataframe()
    data = json.loads(dataset)
    MP_00 = pd.read_json(data['df_00'], orient='split')
    trace0 = []

    for item in selected_dropdown_value:
        # Create and style traces
        trace0.append(go.Scatter(
            x=MP_00['time'],
            y=MP_00[item],
            name=item + ' Before First Stand',
            text=MP_00[item],
            line=dict(
                # color=('rgb(205, 12, 24)'),
                dash='solid',
                width=2)
        ))

    traces = [trace0]
    data = [val for sublist in traces for val in sublist]

    # Edit the layout
    layout = dict(title='Process Data Before First stands "{}"'.format(selected_dropdown_value),
                  xaxis={"title": "Date Time",
                         'rangeselector': {'buttons': list([
                             {'count': 1, 'label': '1M', 'step': 'minute', 'stepmode': 'backward'},
                             {'count': 10, 'label': '6M', 'step': 'minute', 'stepmode': 'backward'},
                             {'step': 'all'}
                         ])}, 'rangeslider': {'visible': False}, 'type': 'date'},
                  # yaxis=dict(title='Values'),
                  margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                  legend={'x': 0, 'y': 1},
                  hovermode='closest'
                  )

    # Plot and embed
    fig = dict(data=data, layout=layout)
    return fig


'''
    Last stand Plotting
'''


@app.callback(
    Output('afterlaststand_plot', 'figure'),
    [Input('afterlaststand-list', 'value'), Input("interval_pseg", "n_intervals")])
def display_value(selected_dropdown_value, _):
    dataset = get_dataframe()
    data = json.loads(dataset)
    MP_10 = pd.read_json(data['df_10'], orient='split')
    # MP_01.to_csv('data', sep='\t', encoding='utf-8')
    # index = pd.to_datetime(MP_02['time'], format="%Y-%m-%d %H:%M:%S.%f")
    trace10 = []

    for item in selected_dropdown_value:
        trace10.append(go.Scatter(
            x=MP_10['time'],
            y=MP_10[item],
            name=item + ' After Last Stand',
            text=MP_10[item],
            line=dict(
                #  color=('rgb(22, 96, 167)'),
                width=2,
                dash='solid')
        ))
    traces = [trace10]
    data = [val for sublist in traces for val in sublist]

    # Edit the layout
    layout = dict(title='Process Data After Last stands "{}"'.format(selected_dropdown_value),
                  xaxis={"title": "Date Time",
                         'rangeselector': {'buttons': list([
                             {'count': 1, 'label': '1M', 'step': 'minute', 'stepmode': 'backward'},
                             {'count': 10, 'label': '6M', 'step': 'minute', 'stepmode': 'backward'},
                             {'step': 'all'}
                         ])}, 'rangeslider': {'visible': False}, 'type': 'date'},
                  # yaxis=dict(title='Values'),
                  margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                  legend={'x': 0, 'y': 1},
                  hovermode='closest'
                  )

    # Plot and embed
    fig = dict(data=data, layout=layout)
    return fig
