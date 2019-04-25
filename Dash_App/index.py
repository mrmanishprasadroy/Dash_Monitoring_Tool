import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import segment_data, measurement_data, strip_tracking, process_data, setup_table, coiler_tracking, coilid_tracking
from segmentdata import *
from measurment_data import *
from srtip_tracking_data import *
from setup_data import *
from coiler_exit_data import *
from coil_id_tracking_data import *

process_dateset = read_segment_data_monitor()
meas_data = read_measurment_data()
strip_dataset = read_strip_tracking_data()
coiler_dataset = read_data()
# setup_dataset = setup_data()

app.layout = html.Div([
    # header
    html.Div([

        html.Span("PLTCM  Monitoring Tool", className='app-title'),
        html.Div(
            html.Img(
                src='assets/logo.png',
                height="100%")
            , style={"float": "right", "height": "80%", "padding": "5px"})
    ],
        className="row header"
    ),
    dcc.Location(id='url', refresh=False),
    # indicators row div
    html.Div(
        [
            dcc.Link('Segment Data Monitor', href='/apps/segment_data', className='button'),
            dcc.Link('Measurment Data Monitor', href='/apps/measurement_data', className='button'),
            dcc.Link('Strip Tracking Monitor', href='/apps/strip_tracking', className='button'),
            dcc.Link('Process Data Monitor', href='/apps/process_data', className='button'),
            dcc.Link('Setup Data Monitor', href='/apps/setup_data', className='button'),
            dcc.Link('Exit Area Monitor', href='/apps/exit_area', className='button'),
            dcc.Link('Coil Id Tracking', href='/apps/coilid_tracking', className='button'),
        ], className="row", ),
    # Hidden divs to contain data
    html.Div(process_dateset, id="segment_dataset_df", style={'display': "none"}),
    html.Div(meas_data, id="meas_dataset_df", style={'display': "none"}),
    html.Div(strip_dataset, id="strip_dataset_df", style={'display': "none"}),
    html.Div(process_dateset, id="process_dataset_df", style={'display': "none"}),
    html.Div(coiler_dataset, id="coiler_dataset_df", style={'display': "none"}),
    html.Div(read_coilid_data(), id="coilTrack_dataset_df", style={'display': "none"}),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/segment_data':
        return segment_data.layout
    elif pathname == '/apps/measurement_data':
        return measurement_data.layout
    elif pathname == '/apps/strip_tracking':
        return strip_tracking.layout
    elif pathname == '/apps/process_data':
        return process_data.layout
    elif pathname == '/apps/setup_data':
        return setup_table.layout
    elif pathname == '/apps/exit_area':
        return coiler_tracking.layout
    elif pathname == '/apps/coilid_tracking':
        return coilid_tracking.layout
    else:
        return segment_data.layout


if __name__ == '__main__':
    app.run_server(host='10.182.10.162', debug=True)
