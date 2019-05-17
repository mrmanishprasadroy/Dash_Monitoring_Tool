import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import json
from app import app
import pandas as pd
import os
import redis
import tasks

redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])

tasks.update_strip_data()


def get_dataframe():
    """Retrieve the dataframe from Redis
    This dataframe is periodically updated through the redis task
    """
    jsonified_df = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["STRIPDATA"]
    ).decode("utf-8")
    # df = pd.DataFrame(json.loads(jsonified_df))
    return json.loads(jsonified_df)


def serve_layout():
    return html.Div([
        dcc.Dropdown(
            id='stand-dropdown',
            options=[
                {'label': '{}'.format(i), 'value': i} for i in [
                    'Stand 1', 'Stand 2', 'Stand 3', 'Stand 4', 'Stand 5'
                ]
            ],
            multi=True,
            value=['Stand 1', 'Stand 2', 'Stand 3', 'Stand 4', 'Stand 5']
        ),
        html.Div(id="status_strip"),
        # Interval
        dcc.Interval(interval=30 * 1000, id="interval_strip"),
        # Chart Container
        html.Div(
            [
                dcc.Graph(
                    id="strip_plot",
                    config=dict(displayModeBar=False),
                ),
            ], className="row", style={"marginBottom": "10"}
        ),

        # Chart Container
        html.Div(
            [
                dcc.Graph(
                    id="coil_plot",
                    config=dict(displayModeBar=False),
                ),
            ], className="row", style={"marginBottom": "10"}
        )
    ])



@app.callback(
    Output('strip_plot', 'figure'),
    [Input('stand-dropdown', 'value'), Input('interval_strip', 'n_intervals')])
def display_value(selected_value, _):
    dataset = get_dataframe()
    data = json.loads(dataset)
    df_bigdata = pd.read_json(data['df_02'], orient='split')
    df_bigdata = df_bigdata.reset_index()
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
    layout = dict(title='InMillExitLengthAtStand "{}"'.format(selected_value),
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
    Output('coil_plot', 'figure'),
    [Input('stand-dropdown', 'value'), Input('interval_strip', 'n_intervals')])
def display_coil_value(selected_value, _):
    dataset = get_dataframe()
    data = json.loads(dataset)
    df_bigdata = pd.read_json(data['df_01'], orient='split')
    df_bigdata = df_bigdata.reset_index()
    index = df_bigdata['timeIndex']
    coil_1 = df_bigdata['Coil 1'] / 1000
    coil_2 = df_bigdata['Coil 2'] / 1000
    # Create and style traces
    trace0 = go.Scatter(
        x=index,
        y=coil_1,
        name='Coil 1',
        text=coil_1,
        line=dict(
            # color=('rgb(205, 12, 24)'),
            # dash='dash',
            width=4)
    )

    # Create and style traces
    trace1 = go.Scatter(
        x=index,
        y=coil_2,
        name='Coil 2',
        text=coil_2,
        line=dict(
            # color=('rgb(205, 12, 24)'),
            # dash='dash',
            width=4)
    )

    data = [trace0, trace1]

    # Edit the layout
    Layout = dict(title='InMillDistSyncToStripEnd',
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


@app.callback(
    Output("status_strip", "children"),
    [Input("interval_strip", "n_intervals")],
)
def update_status(_):
    data_last_updated = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["STRIPDATA_DATE_UPDATED"]
    ).decode("utf-8")

    return "Data last updated at {}".format(data_last_updated)
