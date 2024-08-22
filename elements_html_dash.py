import dash
import aiohttp
import asyncio
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, State
from dash.dependencies import Input, Output
import dash_tvlwc

input_tiker = dbc.Input(id="input-tiker", type="str", placeholder="SBER",
                        valid=False, class_name="form-control is-invalid ",
                        style={"font-size": "1.6rem", "width": "100%"})
label_output_tiker = dbc.Label(id='label_output_tiker')
button_enter = dbc.Button(id="button-enter",children="Enter",n_clicks=0,
                            size="lg",style={"font-size": "1.6rem", "width": "20%"}, color="primary", className="me-md-2")
