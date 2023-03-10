# External package imports
import dash_bootstrap_components as dbc
from dash import html, dcc

# Python Imports
from datetime import datetime
from datetime import date

# Local Imports
from dashboard.config import config


danger_modal = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Network Error")),
        dbc.ModalBody(dbc.Alert("Network failure. Please try again.")),
        dbc.ModalFooter(
            dbc.Button(
                "Close", id="close", className="ms-auto", n_clicks=0, disabled=True
            )
        ),
    ],
    id="modal",
    is_open=False,
)

search_bar = dbc.Row(
    [
        dcc.DatePickerSingle(
            id='my-date-picker-single',
            min_date_allowed=date(2022, 12, 31),
            max_date_allowed=date(int(datetime.now().year), int(datetime.now().month), int(datetime.now().day)),
            initial_visible_month=date(int(datetime.now().year), int(datetime.now().month), int(datetime.now().day)),
            date=date(int(datetime.now().year), int(datetime.now().month), int(datetime.now().day)),
        )
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="right",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=config.SNOLAB_LOGO, height="80px", alt="homepage", className="dark-logo")),
                        dbc.Col(dbc.NavbarBrand("Seismic Events & Activities", className="ms-2 fs-3")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://snolab.ca",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)
