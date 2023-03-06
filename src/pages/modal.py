# External package imports
import dash_bootstrap_components as dbc


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
