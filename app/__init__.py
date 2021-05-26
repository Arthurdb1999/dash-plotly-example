# This Python file uses the following encoding: utf-8
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Import dos layouts
from app.frontend import main
from app.backend.callbacks import *
from app.server import app, server

# Leitura dos dados que serão utilizados (é ideal que estes estejam em uma BD)
data = pd.read_csv('app/backend/data/caso.csv')

# Describe the layout UI of the app
app.layout = html.Div([
    # Este componente serve para inicializar outros componentes, se necessário
    dcc.Interval(id='interval-component', interval=1000,
                    n_intervals=0, max_intervals=0),

    dcc.Location(id="url", refresh=False),

    html.Div(id="page-content",
            # Classes de bootstrap usadas para responsividade
            className="col-lg-8 col-md-8 col-sm-10 col-12 m-2 border"
    )
], className="d-flex justify-content-center")


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return main.layout
    '''
    if pathname == "/route_name":
        return route_name.layout
    '''
    return None

app.config.suppress_callback_exceptions = True
