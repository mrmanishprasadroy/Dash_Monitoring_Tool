import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import json
from app import app,dbc
import pandas as pd
import os
import redis
import tasks

redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])

tasks.update_coiler_data()


def get_dataframe():
    """Retrieve the dataframe from Redis
    This dataframe is periodically updated through the redis task
    """
    jsonified_df = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["COILERDATA"]
    ).decode("utf-8")
    # df = pd.DataFrame(json.loads(jsonified_df))
    return json.loads(jsonified_df)


first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Exit Plot", className="card-title"),
            dcc.Graph(
                id="exit_plot",
                config=dict(displayModeBar=False),
            ),
        ]
    )
)


second_card = dbc.Card(
    dbc.CardBody(
        [
            dbc.Alert("Select From DropDown", color="info"),
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
            html.H5("Exit Coilid Plot", className="card-title"),
            dcc.Graph(
                id="coilid_plot",
                config=dict(displayModeBar=False),
            ),
        ]
    )
)

def serve_layout():
    return html.Div([

        dbc.Alert(id="status_coiler",color="success"),
        # Interval
        dcc.Interval(interval=30 * 1000, id="interval_coiler"),
        dbc.Row([dbc.Col(first_card, width=6), dbc.Col(second_card, width=6)]),
    ])


@app.callback(
    Output('exit_plot', 'figure'),
    [Input('exitarea-dropdown', 'value'), Input('interval_coiler', 'n_intervals')])
def display_value(selected_value, _):
    dataset = get_dataframe()
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
                width=2)
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
                         ])}, 'rangeslider': {'visible': False}, 'type': 'date'},
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
    [Input('exitarea-dropdown', 'value'),  Input('interval_coiler', 'n_intervals')])
def display_coil_value(selected_value, _):
    dataset = get_dataframe()
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
            dash='solid',
            width=2)
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
            width=2)
    )

    data = [trace0, trace1]

    # Edit the layout
    Layout = dict(title='coil id out',
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
    fig = dict(data=data, layout=Layout)
    return fig


@app.callback(
    Output("status_coiler", "children"),
    [Input('interval_coiler', 'n_intervals')],
)
def update_status(_):
    data_last_updated = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["COILERDATA_DATE_UPDATED"]
    ).decode("utf-8")

    return "Data last updated at {}".format(data_last_updated)
