import dash
import aiohttp
import asyncio
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, State
from dash.dependencies import Input, Output
import dash_tvlwc
from  tinkoff_get_func import get_sandels_day

data1 = get_sandels_day('SBER')
app = dash.Dash(__name__)

app.layout = html.Div( children=[
    dcc.Input(id="input-1", type="str",style={"font-size": "1.6rem"}),
    dbc.Button(
    id="button-1",
    children="Enter",
    n_clicks=0,
    size="lg",
    style={"font-size": "1.6rem"},
    color="primary",
    className="me-md-2",
    ),
    dbc.Button("1m", id='time-frame1m', color="blue", size="lg", style={"font-size": "1.6rem"},className="me-md-2"),
    dbc.Button("5m", id='time-frame5m', color="blue", size="lg", style={"font-size": "1.6rem"},className="me-md-2"),
    dbc.Button("1h", id='time-frame30m', color="blue", size="lg", style={"font-size": "1.6rem"},className="me-md-2"),
    dbc.Button("1d", id='time-frame1h', color="blue", size="lg", style={"font-size": "1.6rem"},className="me-md-2"),
    dash_tvlwc.Tvlwc(
        id='chart',
        seriesData=[data1],
        seriesTypes=['candlestick'],
        width= '100vw',
        height='700px',#'400px'

    )
])

buttons = html.Div(
    [
        # dbc.Button("Primary", color="primary", className="me-1"),
        # dbc.Button("Secondary", color="secondary", className="me-1"),
        # dbc.Button("Success", color="success", className="me-1"),
        # dbc.Button("Warning", color="warning", className="me-1"),
        # dbc.Button("Danger", color="danger", className="me-1"),
        dbc.Button("1m", id='time-frame1m', color="info", className="me-1"),
        dbc.Button("5m", id='time-frame5m', color="info", className="me-1"),
        dbc.Button("1h", id='time-frame1h', color="info", className="me-1"),
        dbc.Button("1d", id='time-frame1d', color="info", className="me-1"),
        # dbc.Button("Light", color="light", className="me-1"),
        # dbc.Button("Dark", color="dark", className="me-1"),
        # dbc.Button("Link", color="link"),
    ]
)


@app.callback(
    Output('chart', 'seriesData'),
    Input("button-1", 'n_clicks'),
    # Input('time-frame5m', 'n_clicks'),
    # Input('time-frame1m', 'n_clicks'),
    # Input('time-frame1h', 'n_clicks'),
    # Input('time-frame1d', 'n_clicks'),
    State("input-1", 'value'),
    prevent_initial_call=True
)
def on_button_click(n_clicks, value):
    print(value)
    data = get_sandels_day(value)
    return [data] if data else None
    # return
# if __name__ == "__main__":
#     app.run_server(debug=True, host="0.0.0.0", port=8000)
