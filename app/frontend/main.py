from app.server import app

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([

    html.Div([

        html.P("Título Seção",
               className='text-center font-weight-bold text-uppercase col-12 my-2'),

        dcc.Loading([

            dcc.Dropdown(id="main_dropdown_states"),

            dcc.Graph(id='main_graph_1', className="col-12"),

            dcc.Graph(id='main_graph_2', className="col-12"),
            
            dcc.Graph(id='main_graph_3', className="col-12"),
        ]),

    ], className="col-12 m-0")

], className="")
