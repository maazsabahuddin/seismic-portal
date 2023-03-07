# Python imports
import dash
from datetime import date

# Local Imports
from src.pages import components
from src.utils import request_utils
from src.config import config

# Framework Imports
import dash_bootstrap_components as dbc
from dash import dcc, html, Output, Input, State, callback
import plotly.express as px


dash.register_page(__name__, title="Seismic Events Dashboard")


def get_dataframe(_date=None):
    """
    This function is responsible to return a dataframe object by fetching data from backend.
    :param _date:
    :return:
    """
    return request_utils.request_seismic_data(date=_date)


dataframe_obj, status, date_fetched = get_dataframe(_date=date.today().strftime("%Y-%m-%d"))


def display_graph(y_axis=None, title=None, df=None):
    """
    This function will be displaying the graph.
    :param y_axis:
    :param title:
    :param df:
    :return:
    """
    fig = px.line(df, x='datetime', y=y_axis, title=title, template="plotly_dark", labels={
                     "datetime": "Time",
                     y_axis: "PPV (mm/s)"
                 })
    fig.update_layout(yaxis_range=[0, 0.003])
    return fig


def graph_figure():
    return {}


layout = html.Div([

    html.Center(components.danger_modal),

    dcc.Loading(
        id="loading-1",
        type="default",
        children=[
            dbc.Row([
                dbc.Col(dcc.Graph(id="graph1", figure=graph_figure()), width=12),
            ])
        ]
    ),
    dcc.Loading(
        id="loading-2",
        type="default",
        children=[
            dbc.Row([
                dbc.Col(dcc.Graph(id="graph2", figure=graph_figure()), width=12),
            ], className="py-2")
        ]
    ),
    dcc.Loading(
        id="loading-3",
        type="default",
        children=[
            dbc.Row([
                dbc.Col(dcc.Graph(id="graph3", figure=graph_figure()), width=12),
            ])
        ]
    ),
    dcc.Loading(
        id="loading-4",
        type="default",
        children=[
            dbc.Row([
                dbc.Col(dcc.Graph(id="graph4", figure=graph_figure()), width=12),
            ], className="pt-2")
        ]
    ),

], className="wrapper container pt-4")


@callback(
    [Output(component_id='graph1', component_property='figure'),
     Output(component_id='graph2', component_property='figure'),
     Output(component_id='graph3', component_property='figure'),
     Output(component_id='graph4', component_property='figure'),
     Output(component_id="modal", component_property="is_open")],

    [Input('my-date-picker-single', 'date'),
     Input("close", "n_clicks")],

    [State("modal", "is_open")]
)
def update_output_graph1(date_value, n_clicks_close, is_open):
    """
    This function will be responsible to send the updated data to graphs.
    :param date_value:
    :param n_clicks_close:
    :param is_open:
    :return:
    """
    if date_value is not None:
        date_object = date.fromisoformat(date_value)
        date_value = date_object.strftime('%Y-%m-%d')

    if n_clicks_close or date.today().strftime("%Y-%m-%d") < date_value:
        return display_graph(y_axis='paladin1_geophone1', title="Paladin1 Geophone", df=config.GRAPH_STATIC_DATA), \
            display_graph(y_axis='paladin1_fba1', title="Paladin1 FBA", df=config.GRAPH_STATIC_DATA), \
            display_graph(y_axis='paladin2_geophone1', title="Paladin2 Geophone", df=config.GRAPH_STATIC_DATA), \
            display_graph(y_axis='paladin2_fba1', title="Paladin2 FBA", df=config.GRAPH_STATIC_DATA), \
            not is_open

    # Fetch data from Server is the date is different
    global dataframe_obj, status, date_fetched
    if date_value != date_fetched:
        dataframe_obj, status, date_fetched = get_dataframe(_date=date_value)

    # Return statement - return data to graph.
    return display_graph(y_axis='paladin1_geophone', title="Paladin1 Geophone", df=dataframe_obj),\
        display_graph(y_axis='paladin1_fba', title="Paladin1 FBA", df=dataframe_obj), \
        display_graph(y_axis='paladin2_geophone', title="Paladin2 Geophone", df=dataframe_obj), \
        display_graph(y_axis='paladin2_fba', title="Paladin2 FBA", df=dataframe_obj), \
        not is_open if not status else is_open
