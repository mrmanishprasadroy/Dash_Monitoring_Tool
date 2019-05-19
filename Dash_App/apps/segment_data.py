import json
import redis
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from telegram_definition_L1 import *
from app import app
import os
import tasks

redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])

#tasks.update_segment_data()


def get_dataframe():
    """Retrieve the dataframe from Redis
    This dataframe is periodically updated through the redis task
    """
    jsonified_df = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["DATASEGMENT"]
    ).decode("utf-8")
    # df = pd.DataFrame(json.loads(jsonified_df))
    return json.loads(jsonified_df)


def serve_layout():
    return html.Div([
        # third Controls
        html.Div(
            [
                dcc.Dropdown(
                    id='item-list',
                    options=[
                        {'label': '{}'.format(teltype_M21[i][0]), 'value': teltype_M21[i][0]} for i in range(0, 13)
                    ],
                    multi=True,
                    value=[teltype_M21[0][0]]
                ),
                html.Div(id="status_seg"),
            ], className="row", style={"marginBottom": "10"}
        ),
        # Interval
        dcc.Interval(interval=30 * 1000, id="interval_seg"),
        # Chart Container
        html.Div(
            [
                dcc.Graph(
                    id="segment_plot",
                    config=dict(displayModeBar=False),
                ),
            ], className="sms_chart_div", style={"marginBottom": "10"}
        )
    ])



@app.callback(
    Output('segment_plot', 'figure'),
    [Input('item-list', 'value'), Input("interval_seg", "n_intervals")])
def display_value(selected_dropdown_value, _):
    dataset = get_dataframe()
    data = json.loads(dataset)
    MP_00 = pd.read_json(data['df_00'], orient='split')
    MP_01 = pd.read_json(data['df_01'], orient='split')
    MP_02 = pd.read_json(data['df_02'], orient='split')
    MP_03 = pd.read_json(data['df_03'], orient='split')
    MP_04 = pd.read_json(data['df_04'], orient='split')
    MP_05 = pd.read_json(data['df_05'], orient='split')
    MP_06 = pd.read_json(data['df_06'], orient='split')
    MP_07 = pd.read_json(data['df_07'], orient='split')
    MP_08 = pd.read_json(data['df_08'], orient='split')
    MP_09 = pd.read_json(data['df_09'], orient='split')
    MP_10 = pd.read_json(data['df_10'], orient='split')
    # MP_01.to_csv('data', sep='\t', encoding='utf-8')
    # index = pd.to_datetime(MP_02['time'], format="%Y-%m-%d %H:%M:%S.%f")
    trace0 = []
    trace1 = []
    trace2 = []
    trace3 = []
    trace4 = []
    trace5 = []
    trace6 = []
    trace7 = []
    trace8 = []
    trace9 = []
    trace10 = []

    for item in selected_dropdown_value:
        # Create and style traces
        trace0.append(go.Scatter(
            x=MP_00['time'],
            y=MP_00[item],
            name=item + ' at MP 00',
            text=MP_00[item],
            line=dict(
                # color=('rgb(205, 12, 24)'),
                dash='dash',
                width=4)
        ))
        trace1.append(go.Scatter(
            x=MP_01['time'],
            y=MP_02[item],
            name=item + ' at MP 01',
            text=MP_01[item],
            line=dict(
                # color=('rgb(22, 96, 167)'),
                dash='dash',
                width=4, )
        ))
        trace2.append(go.Scatter(
            x=MP_02['time'],
            y=MP_02[item],
            name=item + 'at MP 02',
            text=MP_02[item],
            line=dict(
                # color=('rgb(205, 12, 24)'),
                width=4,
                dash='dash')  # dash options include 'dash', 'dot', and 'dashdot'
        ))
        trace3.append(go.Scatter(
            x=MP_03['time'],
            y=MP_03[item],
            name=item + ' at MP 03',
            text=MP_03[item],
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=4,
                dash='dash')
        ))
        trace4.append(go.Scatter(
            x=MP_04['time'],
            y=MP_04[item],
            name=item + ' at MP 04',
            text=MP_04[item],
            line=dict(
                # color=('rgb(205, 12, 24)'),
                width=4,
                dash='dash')
        ))
        trace5.append(go.Scatter(
            x=MP_05['time'],
            y=MP_06[item],
            name=item + ' at MP 05',
            text=MP_05[item],
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=4,
                dash='dash')
        ))
        trace6.append(go.Scatter(
            x=MP_06['time'],
            y=MP_06[item],
            name=item + ' at MP 06',
            text=MP_06[item],
            line=dict(
                #  color=('rgb(22, 96, 167)'),
                width=4,
                dash='dash')
        ))
        trace7.append(go.Scatter(
            x=MP_07['time'],
            y=MP_08[item],
            name=item + ' at MP 07',
            text=MP_07[item],
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=4,
                dash='dash')
        ))
        trace8.append(go.Scatter(
            x=MP_08['time'],
            y=MP_08[item],
            name=item + ' at MP 08',
            text=MP_08[item],
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=4,
                dash='dash')
        ))
        trace9.append(go.Scatter(
            x=MP_09['time'],
            y=MP_09[item],
            name=item + ' at MP 09',
            text=MP_09[item],
            line=dict(
                #  color=('rgb(22, 96, 167)'),
                width=4,
                dash='dot')
        ))
        trace10.append(go.Scatter(
            x=MP_10['time'],
            y=MP_10[item],
            name=item + ' at MP 10',
            text=MP_10[item],
            line=dict(
                #  color=('rgb(22, 96, 167)'),
                width=4,
                dash='dot')
        ))
    traces = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9,trace10]
    data = [val for sublist in traces for val in sublist]

    # Edit the layout
    layout = dict(title='Segment data at measurement points "{}"'.format(selected_dropdown_value),
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
    Output("status_seg", "children"),
    [Input('item-list', 'value'), Input("interval_seg", "n_intervals")],
)
def update_status(value, _):
    data_last_updated = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["SEGMENT_DATE_UPDATED"]
    ).decode("utf-8")

    return "Data last updated at {}".format(data_last_updated)