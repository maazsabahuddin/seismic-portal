# External package imports
import dash_bootstrap_components as dbc
from dash import html, dcc
from datetime import date
from src.config import config

SNOLAB_LOGO = "https://www.cap.ca/wp-content/uploads/2017/03/snolab-logo-websize-2.jpg"

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
            min_date_allowed=date(2017, 9, 19),
            max_date_allowed=date(int(config.year), int(config.month), int(config.day)),
            initial_visible_month=date(int(config.year), int(config.month), int(config.day)),
            date=date(int(config.year), int(config.month), int(config.day)),
        ),
        # dbc.Col(dbc.Input(id="input-on-submit", type="text", placeholder="Search", value=config.global_date)),
        # dbc.Col(
        #     dbc.Button(
        #         "Update", color="primary", className="ms-2", n_clicks=0, id="submit-val"
        #     ),
        #     width="auto",
        # ),
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
                        dbc.Col(html.Img(src=SNOLAB_LOGO, height="40px")),
                        dbc.Col(dbc.NavbarBrand("Seismic Events & Activities", className="ms-2")),
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
