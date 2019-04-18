import json

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from app import app

layout = [
    # third Controls
    html.Div(
        [
            dcc.Dropdown(
                id='item-list',
                options=[
                    {'label': '{}'.format(i), 'value': i} for i in [
                        'SegId', 'SetupId', 'LenSegStart', 'TmSinceThread', 'LenSeg', 'TmSeg', 'VolSeg', 'NumValSeg'
                    ]
                ],
                multi=True,
                value=['SegId']
            ),
        ], className="row", style={"marginBottom": "10"}
    ),

    # Chart Container
    html.Div(
        [
            dcc.Graph(
                id="segment_plot",
                config=dict(displayModeBar=False),
            ),
        ], className="sms_chart_div", style={"marginBottom": "10"}
    )
]


@app.callback(
    Output('segment_plot', 'figure'),
    [Input('item-list', 'value'), Input('segment_dataset_df', 'children')])
def display_value(selected_dropdown_value, dataset):
    data = json.loads(dataset)
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

    for item in selected_dropdown_value:
        # Create and style traces
        trace0.append(go.Scatter(
            x=MP_01['time'],
            y=MP_01[item],
            name=item + ' at MP 01',
            line=dict(
                # color=('rgb(205, 12, 24)'),
                dash='dash',
                width=4)
        ))
        trace1.append(go.Scatter(
            x=MP_02['time'],
            y=MP_02[item],
            name=item + ' at MP 02',
            line=dict(
                # color=('rgb(22, 96, 167)'),
                dash='dash',
                width=4, )
        ))
        trace2.append(go.Scatter(
            x=MP_03['time'],
            y=MP_03[item],
            name=item + 'at MP 03',
            line=dict(
                # color=('rgb(205, 12, 24)'),
                width=4,
                dash='dash')  # dash options include 'dash', 'dot', and 'dashdot'
        ))
        trace3.append(go.Scatter(
            x=MP_04['time'],
            y=MP_04[item],
            name=item + ' at MP 04',
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=4,
                dash='dash')
        ))
        trace4.append(go.Scatter(
            x=MP_05['time'],
            y=MP_05[item],
            name=item + ' at MP 05',
            line=dict(
                # color=('rgb(205, 12, 24)'),
                width=4,
                dash='dash')
        ))
        trace5.append(go.Scatter(
            x=MP_06['time'],
            y=MP_06[item],
            name=item + ' at MP 06',
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=4,
                dash='dash')
        ))
        trace6.append(go.Scatter(
            x=MP_07['time'],
            y=MP_07[item],
            name=item + ' at MP 07',
            line=dict(
                #  color=('rgb(22, 96, 167)'),
                width=4,
                dash='dash')
        ))
        trace7.append(go.Scatter(
            x=MP_08['time'],
            y=MP_08[item],
            name=item + ' at MP 08',
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=4,
                dash='dash')
        ))
        trace8.append(go.Scatter(
            x=MP_09['time'],
            y=MP_09[item],
            name=item + ' at MP 09',
            line=dict(
                # color=('rgb(22, 96, 167)'),
                width=4,
                dash='dash')
        ))
        trace9.append(go.Scatter(
            x=MP_10['time'],
            y=MP_10[item],
            name=item + ' at MP 10',
            line=dict(
                #  color=('rgb(22, 96, 167)'),
                width=4,
                dash='dot')
        ))
    traces = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9]
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
