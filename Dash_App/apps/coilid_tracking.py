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

tasks.update_coil_data()


def get_dataframe():
    """Retrieve the dataframe from Redis
    This dataframe is periodically updated through the redis task
    """
    jsonified_df = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["COILDATA"]
    ).decode("utf-8")
    # df = pd.DataFrame(json.loads(jsonified_df))
    return json.loads(jsonified_df)


def serve_layout():
    return html.Div([
        dcc.Dropdown(
            id='coilid-dropdown',
            options=[
                {'label': '{}'.format(i), 'value': i} for i in [
                    'coil_1', 'coil_2', 'coil_3', 'coil_4', 'coil_5', 'coil_6', 'coil_7', 'coil_8',
                    'coil_9', 'coil_10', 'coil_11', 'coil_12'
                ]
            ],
            multi=True,
            value=['coil_1', 'coil_2', 'coil_3', 'coil_4', 'coil_5', 'coil_6', 'coil_7', 'coil_8']
        ),
        html.Div(id="status_coilid"),
        # Interval
        dcc.Interval(interval=30 * 1000, id="interval_coilid"),
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
    [Input('coilid-dropdown', 'value'), Input('interval_coilid', 'n_intervals')])
def display_value(selected_value, _):
    dataset = get_dataframe()
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


@app.callback(
    Output("status_coilid", "children"),
    [Input('interval_coilid', 'n_intervals')],
)
def update_status(_):
    data_last_updated = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["COILDATA_DATE_UPDATED"]
    ).decode("utf-8")

    return "Data last updated at {}".format(data_last_updated)
