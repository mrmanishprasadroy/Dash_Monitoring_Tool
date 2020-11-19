import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, dbc
from apps import segment_data, measurement_data, strip_tracking, process_data, setup_table, coiler_tracking, \
    coilid_tracking

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#cbd3da",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "25rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        dbc.CardImg(src="assets/logo.png", top=True),
        html.H2("PLTCM Monitoring", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink('Segment Data ', href='/apps/segment_data'),
                dbc.NavLink('Measurements Data ', href='/apps/measurement_data'),
                dbc.NavLink('Strip Tracking ', href='/apps/strip_tracking'),
                dbc.NavLink('Process Data ', href='/apps/process_data'),
                dbc.NavLink('Setup Data ', href='/apps/setup_data'),
                dbc.NavLink('Exit Area Tracking', href='/apps/exit_area'),
                dbc.NavLink('CoilId Tracking', href='/apps/coilid_tracking'),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
app.title = 'XSense'


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/apps/segment_data"]:
        return segment_data.serve_layout()
    elif pathname == "/apps/measurement_data":
        return measurement_data.serve_layout()
    elif pathname == "/apps/strip_tracking":
        return strip_tracking.serve_layout()
    elif pathname == "/apps/process_data":
        return process_data.serve_layout()
    elif pathname == "/apps/setup_data":
        return setup_table.serve_layout()
    elif pathname == "/apps/exit_area":
        return coiler_tracking.serve_layout()
    elif pathname == "/apps/coilid_tracking":
        return coilid_tracking.serve_layout()
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)
