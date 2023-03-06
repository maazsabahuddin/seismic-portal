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