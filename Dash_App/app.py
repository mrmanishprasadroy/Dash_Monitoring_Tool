import dash
import dash_bootstrap_components as dbc
import flask

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,external_stylesheets=[dbc.themes.FLATLY])

app.config.suppress_callback_exceptions = True
