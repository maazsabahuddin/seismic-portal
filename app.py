# Python imports
import datetime
import requests
import json
import pandas as pd

# Local Imports
from pages import dashboard

# Framework Imports
from dash import Output, Input, State


from dash import Dash, html
import dash


global_date = datetime.date.today().strftime("%Y-%m-%d")
url = "http://127.0.0.1:8000/api"


def request_seismic_data(date):
    """
    This API will request to fetch seismic event data.
    :param date:
    """
    response = requests.get(f"{url}/{'activity'}/?date={date}")
    data = json.loads(response.text)

    return pd.DataFrame(data['responseData'])


app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    dash.page_container
])


@app.callback(
    Output('heading', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output_heading(n_clicks, value):
    if not value or not n_clicks:
        return f'Seismic Events or Activities - {global_date}'
    return f'Seismic Events or Activities - {value}'


@app.callback(
    Output(component_id='graph1', component_property='figure'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output_heading(n_clicks, value):
    print(f"Click: {n_clicks}")
    df = request_seismic_data(date=value)
    return dashboard.display_graph(y_axis='paladin1_geophone1', df=df)


if __name__ == '__main__':
    app.run_server(debug=True)
