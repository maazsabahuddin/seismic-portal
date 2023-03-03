# Python imports
import dash

# Local Imports
import app

# Framework Imports
from dash import dcc, html
import plotly.express as px


dash.register_page(__name__)


def display_graph(y_axis=None, df=None):
    """
    This function will be displaying the graph.
    :param y_axis:
    :param df:
    :return:
    """
    fig = px.line(df, x='datetime', y=y_axis)
    return fig


layout = html.Div([

    html.Center(
        html.H1(children=f'Seismic Events or Activities - {app.global_date}', id="heading"),
    ),
    html.Div(dcc.Input(id='input-on-submit', type='text', value=app.global_date)),
    html.Button('Submit', id='submit-val', n_clicks=0),


    html.H4('Paladin1 Geophone1 Sensor'),
    dcc.Loading(
        id="loading-1",
        type="default",
        children=[
            dcc.Graph(id="graph1", figure={}),
        ]
    ),

    # html.H4('Paladin1 Geophone2 Sensor'),
    # dcc.Graph(id="graph2", figure={}),

    # html.H4('Paladin1 Geophone3 Sensor'),
    # dcc.Graph(id="graph3"),
    #
    # html.H4('Paladin1 FBA1 Sensor'),
    # dcc.Graph(id="graph7"),
    #
    # html.H4('Paladin1 FBA2 Sensor'),
    # dcc.Graph(id="graph8"),
    #
    # html.H4('Paladin1 FBA3 Sensor'),
    # dcc.Graph(id="graph9"),
    #
    # html.H4('Paladin2 Geophone1 Sensor'),
    # dcc.Graph(id="graph4"),
    #
    # html.H4('Paladin2 Geophone2 Sensor'),
    # dcc.Graph(id="graph5"),
    #
    # html.H4('Paladin2 Geophone3 Sensor'),
    # dcc.Graph(id="graph6"),
    #
    # html.H4('Paladin2 FBA1 Sensor'),
    # dcc.Graph(id="graph10"),
    #
    # html.H4('Paladin2 FBA2 Sensor'),
    # dcc.Graph(id="graph11"),
    #
    # html.H4('Paladin2 FBA3 Sensor'),
    # dcc.Graph(id="graph12"),

])
