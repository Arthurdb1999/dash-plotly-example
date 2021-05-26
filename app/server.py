# Dash app initialization
import dash
import dash_bootstrap_components as dbc

# User management initialization
import os

app = dash.Dash(
    __name__,
    meta_tags=[
        {
            'charset': 'utf-8',
        },
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'
        }
    ],
    external_stylesheets=[
        dbc.themes.BOOTSTRAP        
    ],

    external_scripts=[
    ]
)


server = app.server
app.config.suppress_callback_exceptions = True