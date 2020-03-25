import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import segment_data, measurement_data, strip_tracking, process_data, setup_table, coiler_tracking, \
    coilid_tracking


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
            dcc.Link('Segment Data Monitor', href='/apps/segment_data', className='submit button-primary', style={'marginRight': 25}),
            dcc.Link('Measurment Data Monitor', href='/apps/measurement_data', className='submit button-primary', style={'marginRight': 25}),
            dcc.Link('Strip Tracking Monitor', href='/apps/strip_tracking', className='submit button-primary',style={'marginRight': 25}),
            dcc.Link('Process Data Monitor', href='/apps/process_data', className='submit button-primary', style={'marginRight': 25}),
            dcc.Link('Setup Data Monitor', href='/apps/setup_data', className='submit button-primary', style={'marginRight': 25}),
            dcc.Link('Exit Area Monitor', href='/apps/exit_area', className='submit button-primary', style={'marginRight': 25}),
            dcc.Link('Coil Id Tracking', href='/apps/coilid_tracking', className='submit button-primary', style={'marginRight': 25}),
        ], className="row", ),
    # Hidden divs to contain data
    # html.Div(process_dateset, id="process_dataset_df", style={'display': "none"}),
    html.Div(id='page-content',style={'marginBottom': 50, 'marginTop': 25})
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/segment_data':
        return segment_data.serve_layout()
    elif pathname == '/apps/measurement_data':
        return measurement_data.serve_layout()
    elif pathname == '/apps/strip_tracking':
        return strip_tracking.serve_layout()
    elif pathname == '/apps/process_data':
        return process_data.serve_layout()
    elif pathname == '/apps/setup_data':
        return setup_table.serve_layout()
    elif pathname == '/apps/exit_area':
        return coiler_tracking.serve_layout()
    elif pathname == '/apps/coilid_tracking':
        return coilid_tracking.serve_layout()
    else:
        return segment_data.serve_layout()


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)
