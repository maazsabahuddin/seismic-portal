# Python Imports
import datetime

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
