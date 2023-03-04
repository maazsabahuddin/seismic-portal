# Python imports
from pydoc import classname

import dash

# Local Imports
from src.pages.modal import danger_modal
from src.utils import request_utils
from src.config import config

# Framework Imports
import dash_bootstrap_components as dbc
from dash import dcc, html, Output, Input, State, callback
import plotly.express as px


dash.register_page(__name__)


def display_graph(y_axis=None, title=None, df=None):
    """
    This function will be displaying the graph.
    :param y_axis:
    :param title:
    :param df:
    :return:
    """
    fig = px.line(df, x='datetime', y=y_axis, title=title)
    return fig


def graph_figure():
    return {"layout": {"height": 480, "width": 480}}


layout = html.Div([

    html.Center(
        html.H1(children=f'Seismic Events or Activities - {config.global_date}', id="heading"),
    ),
    html.Div(dcc.Input(id='input-on-submit', type='text', value=config.global_date)),
    html.Button('Submit', id='submit-val', n_clicks=0),

    html.Center(danger_modal),
    dcc.Loading(
        id="loading-1",
        type="default",
        children=[
            dbc.Row([
                dbc.Col(dcc.Graph(id="graph1", figure=graph_figure()), width=4),
                dbc.Col(dcc.Graph(id="graph2", figure=graph_figure()), width=4),
                dbc.Col(dcc.Graph(id="graph3", figure=graph_figure()), width=4),
            ])
        ]
    ),
    dcc.Loading(
        id="loading-2",
        type="default",
        children=[
            dbc.Row([
                dbc.Col(dcc.Graph(id="graph4", figure=graph_figure()), width=4),
                dbc.Col(dcc.Graph(id="graph5", figure=graph_figure()), width=4),
                dbc.Col(dcc.Graph(id="graph6", figure=graph_figure()), width=4)
            ])
        ]
    ),
    dcc.Loading(
        id="loading-3",
        type="default",
        children=[
            dbc.Row([
                dbc.Col(dcc.Graph(id="graph7", figure=graph_figure()), width=4),
                dbc.Col(dcc.Graph(id="graph8", figure=graph_figure()), width=4),
                dbc.Col(dcc.Graph(id="graph9", figure=graph_figure()), width=4)
            ])
        ]
    ),
    dcc.Loading(
        id="loading-4",
        type="default",
        children=[
            dbc.Row([
                dbc.Col(dcc.Graph(id="graph10", figure=graph_figure()), width=4),
                dbc.Col(dcc.Graph(id="graph11", figure=graph_figure()), width=4),
                dbc.Col(dcc.Graph(id="graph12", figure=graph_figure()), width=4)
            ])
        ]
    ),

], className="wrapper container")


@callback(
    Output("modal", "is_open"),
    [Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n2, is_open):
    if n2:
        return not is_open

    success = request_utils.check_server_status(url=config.URL)
    if success:
        return is_open
    return not is_open


@callback(
    Output('heading', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)
def update_output_heading(n_clicks, value):
    if not value or not n_clicks:
        return f'Seismic Events or Activities - {config.global_date}'
    return f'Seismic Events or Activities - {value}'


@callback(
    Output(component_id='graph1', component_property='figure'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)
def update_output_graph1(n_clicks, value):
    df, success = request_utils.request_seismic_data(date=value)
    if success:
        return display_graph(y_axis='paladin1_geophone1', title="Paladin1 GP1", df=df)
    return display_graph(y_axis='paladin1_geophone1', title="Paladin1 GP1", df=df)


@callback(
    Output(component_id='graph2', component_property='figure'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)
def update_output_graph1(n_clicks, value):
    df, success = request_utils.request_seismic_data(date=value)
    if success:
        return display_graph(y_axis='paladin1_geophone2', title="Paladin1 GP2", df=df)
    return display_graph(y_axis='paladin1_geophone2', title="Paladin1 GP2", df=df)


@callback(
    Output(component_id='graph3', component_property='figure'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)
def update_output_graph1(n_clicks, value):
    df, success = request_utils.request_seismic_data(date=value)
    if success:
        return display_graph(y_axis='paladin1_geophone3', title="Paladin1 GP3", df=df)
    return display_graph(y_axis='paladin1_geophone3', title="Paladin1 GP3", df=df)


@callback(
    Output(component_id='graph4', component_property='figure'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)
def update_output_graph1(n_clicks, value):
    df, success = request_utils.request_seismic_data(date=value)
    if success:
        return display_graph(y_axis='paladin1_fba1', title="Paladin1 FBA1", df=df)
    return display_graph(y_axis='paladin1_fba1', title="Paladin1 FBA1", df=df)


@callback(
    Output(component_id='graph5', component_property='figure'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)
def update_output_graph1(n_clicks, value):
    df, success = request_utils.request_seismic_data(date=value)
    if success:
        return display_graph(y_axis='paladin1_fba2', title="Paladin1 FBA2", df=df)
    return display_graph(y_axis='paladin1_fba2', title="Paladin1 FBA2", df=df)


@callback(
    Output(component_id='graph6', component_property='figure'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)
def update_output_graph1(n_clicks, value):
    df, success = request_utils.request_seismic_data(date=value)
    if success:
        return display_graph(y_axis='paladin1_fba3', title="Paladin1 FBA3", df=df)
    return display_graph(y_axis='paladin1_fba3', title="Paladin1 FBA3", df=df)


# @callback(
#     Output(component_id='graph7', component_property='figure'),
#     Input('submit-val', 'n_clicks'),
#     State('input-on-submit', 'value'),
#     prevent_initial_call=True
# )
# def update_output_graph1(n_clicks, value):
#     df, success = request_utils.request_seismic_data(date=value)
#     if success:
#         return display_graph(y_axis='paladin2_geophone1', title="Paladin2 GP1", df=df)
#     return display_graph(y_axis='paladin2_geophone1', title="Paladin2 GP1", df=df)
#
#
# @callback(
#     Output(component_id='graph8', component_property='figure'),
#     Input('submit-val', 'n_clicks'),
#     State('input-on-submit', 'value'),
#     prevent_initial_call=True
# )
# def update_output_graph1(n_clicks, value):
#     df, success = request_utils.request_seismic_data(date=value)
#     if success:
#         return display_graph(y_axis='paladin2_geophone2', title="Paladin2 GP2", df=df)
#     return display_graph(y_axis='paladin2_geophone2', title="Paladin2 GP2", df=df)
#
#
# @callback(
#     Output(component_id='graph9', component_property='figure'),
#     Input('submit-val', 'n_clicks'),
#     State('input-on-submit', 'value'),
#     prevent_initial_call=True
# )
# def update_output_graph1(n_clicks, value):
#     df, success = request_utils.request_seismic_data(date=value)
#     if success:
#         return display_graph(y_axis='paladin2_geophone3', title="Paladin2 GP3", df=df)
#     return display_graph(y_axis='paladin2_geophone3', title="Paladin2 GP3", df=df)
#
#
# @callback(
#     Output(component_id='graph10', component_property='figure'),
#     Input('submit-val', 'n_clicks'),
#     State('input-on-submit', 'value'),
#     prevent_initial_call=True
# )
# def update_output_graph1(n_clicks, value):
#     df, success = request_utils.request_seismic_data(date=value)
#     if success:
#         return display_graph(y_axis='paladin2_fba1', title="Paladin2 FBA1", df=df)
#     return display_graph(y_axis='paladin2_fba1', title="Paladin2 FBA1", df=df)
#
#
# @callback(
#     Output(component_id='graph11', component_property='figure'),
#     Input('submit-val', 'n_clicks'),
#     State('input-on-submit', 'value'),
#     prevent_initial_call=True
# )
# def update_output_graph1(n_clicks, value):
#     df, success = request_utils.request_seismic_data(date=value)
#     if success:
#         return display_graph(y_axis='paladin2_fba2', title="Paladin2 FBA2", df=df)
#     return display_graph(y_axis='paladin2_fba2', title="Paladin2 FBA2", df=df)
#
#
# @callback(
#     Output(component_id='graph12', component_property='figure'),
#     Input('submit-val', 'n_clicks'),
#     State('input-on-submit', 'value'),
#     prevent_initial_call=True
# )
# def update_output_graph1(n_clicks, value):
#     df, success = request_utils.request_seismic_data(date=value)
#     if success:
#         return display_graph(y_axis='paladin2_fba3', title="Paladin2 FBA3", df=df)
#     return display_graph(y_axis='paladin2_fba3', title="Paladin2 FBA3", df=df)
