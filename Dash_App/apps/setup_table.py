import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import dash_table
from app import app
import redis
import tasks
from setup_data import *
import flask
import io
from flask import send_file

redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])

tasks.update_setup_data()


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
coil_arr = coils.CoilIdOut.unique()


def serve_layout():
    return html.Div([
        html.Div([
            html.Div(
                dcc.Dropdown(
                    id='coilId',
                    options=[
                        {'label': '{}'.format(i), 'value': i} for i in coil_arr
                    ],
                    value=coil_arr[0]
                ), className="four columns",
            ),
            html.Div(
                html.A('Download Whole Dataset', id='my-link', className='button button-primary'),
                className="four columns"
            ),
            html.Div(id="status"),
        ], className="row"),

        # Interval
        dcc.Interval(interval=30 * 1000, id="interval"),
        # table div
        dcc.Loading(id='table-view', children=html.Div(
            id="setup_table",
            className="row",
            style={
                "maxHeight": "650px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "15",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"

            },
        ),
                    )
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
        sorting=True,
        style_cell={'width': '150px', 'padding': '5px', 'textAlign': 'center'},
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold'
        },
        style_cell_conditional=[{
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
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["DATE_UPDATED"]
    ).decode("utf-8")

    return "Data last updated at {}".format(data_last_updated)