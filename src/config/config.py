# Python Imports
import datetime
import pandas as pd

# Module Imports
from dotenv import dotenv_values
import dash_bootstrap_components as dbc

config = dotenv_values(".env")

# Reading .env variables
URL = config['URL']
ENVIRONMENT = config['ENVIRONMENT']

# Predefined variables
external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
global_date = datetime.date.today().strftime("%Y-%m-%d")

# Static Data
GRAPH_STATIC_DATA = pd.DataFrame([{
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
                    }])


def get_datetime_details():
    """
    This function will return
    """
    from datetime import datetime
    _datetime = datetime.now()
    return _datetime, _datetime.date(), _datetime.year, str(_datetime.month).zfill(2), str(_datetime.day).zfill(2), \
        _datetime.time().replace(microsecond=0)


_dt, date, year, month, day, time = get_datetime_details()

SNOLAB_LOGO = "https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco" \
              ",dpr_1/c06ghtpgpqqm5k8m7z2j"
