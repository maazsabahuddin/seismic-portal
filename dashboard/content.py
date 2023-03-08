# Local Imports
from dashboard.index import app
from dashboard.pages import components

# Framework Imports
from dash import html, page_container


app.layout = html.Div([
    components.navbar,
    page_container,
])
