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
        return find_average_of_each_sensors(df=pd.DataFrame(data['responseData']['results'])), \
            True, data['responseData']['date']
    except Exception as e:
        print(f"Network Error: {e}")
        return config.GRAPH_STATIC_DATA, False, date


def find_average_of_each_sensors(df):
    """
    This function is responsible to take average of 3 columns for every row and make a new column
    :param df:
    """
    df['paladin1_geophone'] = (df['paladin1_geophone1'] + df['paladin1_geophone2'] + df['paladin1_geophone3']) / 3
    df['paladin1_fba'] = (df['paladin1_fba1'] + df['paladin1_fba2'] + df['paladin1_fba3']) / 3
    df['paladin2_geophone'] = (df['paladin2_geophone1'] + df['paladin2_geophone2'] + df['paladin2_geophone3']) / 3
    df['paladin2_fba'] = (df['paladin2_fba1'] + df['paladin2_fba2'] + df['paladin2_fba3']) / 3
    return df
