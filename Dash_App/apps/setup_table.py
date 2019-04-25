import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import dash_table
from app import app
import pandas as pd
from setup_data import *
import flask
import io
from flask import send_file

df_setup = setup_data()
data = json.loads(df_setup)
coils = pd.read_json(data['df_00'], orient='split')
coil_arr = coils.CoilIdOut.unique()
layout = html.Div([
    dcc.Dropdown(
        id='coilId',
        options=[
            {'label': '{}'.format(i), 'value': i} for i in coil_arr
        ],
        value=coil_arr[0]
    ),
    html.A('Download Whole Dataset', id='my-link', className='button'),
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
    excel_data = buf.getvalue()
    buf.seek(0)
    return send_file(
        buf,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        attachment_filename="wholeDataset.xlsx",
        as_attachment=True,
        cache_timeout=0
    )
