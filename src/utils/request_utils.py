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
        response = requests.get(f"{config.URL}api/{'activity'}/?date={date}")
        data = json.loads(response.text)
        print(f"Success: {response}")
        return pd.DataFrame(data['responseData']), True
    except Exception as e:
        print(f"Network Error: {e}")
        return pd.DataFrame([{
            'paladin1_geophone1': 0.0,
            'paladin1_geophone2': 0.0,
            'paladin1_geophone3': 0.0,
            'paladin1_fba1': 0.0,
            'paladin1_fba2': 0.0,
            'paladin1_fba3': 0.0,
            'paladin2_geophone1': 0.0,
            'paladin2_geophone2': 0.0,
            'paladin2_geophone3': 0.0,
            'paladin2_fba1': 0.0,
            'paladin2_fba2': 0.0,
            'paladin2_fba3': 0.0,
            'datetime': '',
        }]), False
