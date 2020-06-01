import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import json
from app import app, dbc
import pandas as pd
import os
import tasks
import redis

redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])

tasks.update_measurment_data()


def get_dataframe():
    """Retrieve the dataframe from Redis
    This dataframe is periodically updated through the redis task
    """
    jsonified_df = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["MESDATA"]
    ).decode("utf-8")
    # df = pd.DataFrame(json.loads(jsonified_df))
    return json.loads(jsonified_df)


first_card = dbc.Card(
    dbc.CardBody(
        [
            dbc.Alert(id="status_meas", color="success"),
            dbc.Alert("Select From DropDown", color="info"),
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
        ]
    )
)


def serve_layout():
    return html.Div([

        # Interval
        dcc.Interval(interval=30 * 1000, id="interval_meas"),
        # Cards
        dbc.Row(
            [
                dbc.Col(dbc.Card(first_card, color="primary", outline=True), width=12)
            ]),

    ])


@app.callback(
    Output('meas_plot', 'figure'),
    [Input('measurment-dropdown', 'value'), Input("interval_meas", "n_intervals")])
def display_value(selected_value, _):
    dataset = get_dataframe()
    data = json.loads(dataset)
    df_bigdata = pd.read_json(data['df_01'], orient='split')
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
                width=2)
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


@app.callback(
    Output("status_meas", "children"),
    [Input("interval_meas", "n_intervals")],
)
def update_status(_):
    data_last_updated = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["MESDATA_DATE_UPDATED"]
    ).decode("utf-8")

    return "Data last updated at {}".format(data_last_updated)
