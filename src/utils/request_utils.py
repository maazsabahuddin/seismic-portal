# Python imports
import requests
import json
import pandas as pd

# Local Imports
from src.config import config


def check_server_status(url):
    try:
        r = requests.head(url)
        return r.status_code == 200
    except Exception as e:
        print(e)
        return False


def request_seismic_data(date):
    """
    This API will request to fetch seismic event data.
    :param date:
    """
    try:
        URL = f"{config.URL}api/{'activity'}/?date={date}"
        response = requests.get(URL)
        data = json.loads(response.text)
        print(f"Success: {response} - {URL}")
        return pd.DataFrame(data['responseData']), True
    except Exception as e:
        print(f"Network Error: {e}")
        return config.GRAPH_STATIC_DATA, False
