import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import dash_table
from app import app, dbc
import redis
import tasks
from setup_data import *
import plotly.graph_objs as go
import flask
import io
from flask import send_file

redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])

tasks.update_setup_data()


# tasks.insert_mongos_db()


def get_dataframe():
    """Retrieve the dataframe from Redis
    This dataframe is periodically updated through the redis task
    """
    jsonified_df = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["DATASETUP"]
    ).decode("utf-8")
    # df = pd.DataFrame(json.loads(jsonified_df))
    return json.loads(jsonified_df)


df_setup = get_dataframe()
data = json.loads(df_setup)
coils = pd.read_json(data['df_00'], orient='split')
col = pd.read_json(data['df_01'], orient='split')
columns = list(col.columns.values)
coil_arr = coils.CoilIdOut.unique()

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Setup  Data", className="card-title"),
            dcc.Dropdown(
                id='coilId',
                options=[
                    {'label': '{}'.format(i), 'value': i} for i in coil_arr
                ],
                value=coil_arr[0]
            ),
            dcc.Loading(id='table-view', children=html.Div(
                id="setup_table",
                # className="row",
                style={
                    "maxHeight": "41rem",
                    "overflowY": "scroll",
                    "padding": "8",
                    "marginTop": "15",
                    "backgroundColor": "white",
                    "border": "1px solid #C8D4E3",
                    "borderRadius": "3px"}), type="cube"),
            html.Div(
                html.A('Download Whole Dataset', id='my-link', className='button button-primary'),
                className="two columns"
            ),

        ]
    )
)

second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("SetUp Varaibal For Plotting", className="card-title"),
            dcc.Dropdown(
                id='Setup_graph',
                options=[
                    {'label': '{}'.format(i), 'value': i} for i in columns
                ],
                multi=True,
                value=[columns[4]]
            ),
            dcc.Graph(
                id="setup_plot",
                config=dict(displayModeBar=False),
            ),
        ]
    )
)


def serve_layout():
    return html.Div([
        # Status
        dbc.Alert(id="status", color='success'),
        # Interval
        dcc.Interval(interval=30 * 1000, id="interval"),
        # Cards
        dbc.Row([dbc.Col(first_card, width=6), dbc.Col(second_card, width=6)])
    ])


# update table based on drop down value and df updates
@app.callback(
    Output("setup_table", "children"),
    [Input("coilId", "value")]
)
def leads_table_callback(value):
    data = json.loads(df_setup)
    df_bigdata = pd.read_json(data['df_01'], orient='split')

    df_bigdata = df_bigdata.loc[df_bigdata['CoilIdOut'] == value]

    datatable = dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df_bigdata.columns],
        data=df_bigdata.to_dict("rows"),
        # n_fixed_rows=1,
        # filtering=True,
        sort_action='native',
        style_cell={'width': '150px', 'padding': '5px', 'textAlign': 'center'},
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold'
        },
        style_data_conditional=[{
            'if': {'row_index': 'odd'},
            'backgroundColor': '#3D9970',
        }],
        style_table={
            'maxHeight': '580px',
            'border': 'thin lightgrey solid'
        },
    )
    return datatable


@app.callback(Output('my-link', 'href'), [Input('coilId', 'value')])
def update_link(value):
    return '/dash/urlToDownload?value={}'.format(1)


@app.server.route('/dash/urlToDownload')
def download_csv():
    value = flask.request.args.get('value')
    data = json.loads(df_setup)
    df = pd.read_json(data['df_01'], orient='split')
    buf = io.BytesIO()
    excel_writer = pd.ExcelWriter(buf, engine="xlsxwriter")
    df.to_excel(excel_writer, sheet_name="sheet1", index=False)
    excel_writer.save()
    buf.seek(0)
    return send_file(
        buf,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        attachment_filename="wholeDataset.xlsx",
        as_attachment=True,
        cache_timeout=0
    )


@app.callback(
    Output("status", "children"),
    [Input("coilId", "value"), Input("interval", "n_intervals")],
)
def update_status(value, _):
    global df_setup
    global coil_arr
    df_setup = get_dataframe()
    data = json.loads(df_setup)
    coils = pd.read_json(data['df_00'], orient='split')
    coil_arr = coils.CoilIdOut.unique()
    data_last_updated = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["SETUP_DATE_UPDATED"]
    ).decode("utf-8")

    return "Data last updated at {}".format(data_last_updated)


@app.callback(
    Output("setup_plot", "figure"),
    [Input("Setup_graph", "value"), Input("interval", "n_intervals")], )
def update_graph_status(selected_dropdown_value, _):
    df_setup = get_dataframe()
    data = json.loads(df_setup)
    df = pd.read_json(data['df_01'], orient='split')
    trace0 = []

    for item in selected_dropdown_value:
        # Create and style traces
        trace0.append(go.Scatter(
            x=df['Time'],
            y=df[item],
            name=item,
            text=df['CoilId'],
            line=dict(
                # color=('rgb(205, 12, 24)'),
                dash='solid',
                width=2)
        ))

    traces = [trace0]
    data = [val for sublist in traces for val in sublist]

    # Edit the layout
    layout = dict(title='Setup Data "{}"'.format(selected_dropdown_value),
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
