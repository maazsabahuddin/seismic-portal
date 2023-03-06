# Local imports
from config import config

# Framework Imports
from dash import Dash, html, page_container


app = Dash(__name__,
           use_pages=True,
           external_stylesheets=config.external_stylesheets,
           title='Seismic Activities',
           meta_tags=[
               {  # check if device is a mobile device. This is a must if you do any mobile styling
                   'name': 'viewport',
                   'content': 'width=device-width, initial-scale=1'
               }
           ])

app.layout = html.Div([
    # page_container
])


if __name__ == '__main__':
    app.run_server(debug=True)
