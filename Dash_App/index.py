import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2
from segmentdata import *
from measurment_data import *

# dateset = read_segment_data_monitor()
# data = json.loads(dataset)
# dff = pd.read_json(datasets['df_1'], orient='split')
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
            dcc.Link('Segment Data Monitor', href='/apps/app1', className='button'),
            dcc.Link('Measurment Data Monitor', href='/apps/app2', className='button'),
        ], className="row", ),
    # Hidden divs to contain data
    html.Div(read_segment_data_monitor(), id="segment_dataset_df", style={'display': "none"}),
    html.Div(read_measurment_data(), id="meas_dataset_df", style={'display': "none"}),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return app1.layout


if __name__ == '__main__':
    app.run_server(debug=True)
