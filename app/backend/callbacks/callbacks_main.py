import numpy as np
import pandas as pd

from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go

# Traz uma instância da aplicação para este arquivo
# É desta forma que é possível adicionar callbacks a nossa aplicação
from app.server import app

# --------------------------------------
# INIT COMPONENTS
# Nesta parte vamos inicializar opções
# --------------------------------------
@app.callback(
    [Output("main_dropdown_states", "options"),
    Output("main_dropdown_states", "value")],
    [Input('interval-component', 'n_intervals')])
def init_dropdown(n_intervals):

    from app import data
    df = data
    states = df['state'].unique()

    options = [{ 'label': state, 'value': state } for state in states]
    value='SC'

    return options, value

# --------------------------------------
# CALLBACKS 
# --------------------------------------
@app.callback(
    Output("main_graph_1", 'figure'),
    [Input('interval-component', 'n_intervals'),
    Input('main_dropdown_states', 'value')])
def update_chart(n_intervals, dropdown_state_value):
    from app import data
    
    # Selecionar dados do dataset
    # Dados do estado de santa catarina geral (por isso city.isnana())
    df = data[['date','state','place_type','deaths']]
    df = df[df['state'] == dropdown_state_value]
    df = df[df['place_type'] == 'state']
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    fig = px.line(df, x ='date', y='deaths', title="Número de óbitos acumulado")
    
    return fig


@app.callback(
    Output("main_graph_2", 'figure'),
    [Input('interval-component', 'n_intervals'),
    Input('main_dropdown_states', 'value')])
def update_chart(n_intervals, dropdown_state_value):
    from app import data
    
    df = data[['date','state','place_type','deaths']]
    df = df[df['state'] == dropdown_state_value]
    df = df[df['place_type'] == 'state']
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df['new_deaths'] = df['deaths'].diff()

    fig = px.line(df, x ='date', y='new_deaths', title="Número de óbitos acumulado")
    
    return fig


@app.callback(
    Output("main_graph_3", 'figure'),
    [Input('interval-component', 'n_intervals'),
    Input('main_dropdown_states', 'value')])
def update_chart(n_intervals, dropdown_state_value):
    from app import data
    
    df = data[['date','state','place_type','deaths']]
    df = df[df['state'] == dropdown_state_value]
    df = df[df['place_type'] == 'state']
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df['new_deaths'] = df['deaths'].diff()
    df['new_deaths_moving_avg_7'] = df['new_deaths'].rolling(7).mean()
    df['new_deaths_moving_avg_14'] = df['new_deaths'].rolling(14).mean()

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            name="Número de óbitos por dia",
            x=df['date'],
            y=df['new_deaths']
        )
    )

    fig.add_trace(
        go.Scatter(
            name="Média móvel de óbitos em 7 dias",
            x=df['date'],
            y=df['new_deaths_moving_avg_7']
        )
    )

    fig.add_trace(
        go.Scatter(
            name="Média móvel de óbitos em 14 dias",
            x=df['date'],
            y=df['new_deaths_moving_avg_14']
        )
    )

    return fig