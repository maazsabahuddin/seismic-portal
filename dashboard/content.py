# Local Imports
from dashboard.index import app
from dashboard.pages import components, graphs

# Framework Imports
from dash import html


app.layout = html.Div([
    components.navbar,
    graphs.layout
])
