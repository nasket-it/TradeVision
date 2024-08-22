import dash
import aiohttp
import asyncio
from func_all import calculate_spread
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, State
from dash.dependencies import Input, Output
import dash_tvlwc
from  tinkoff_get_func import get_tinkoff_chart
from elements_html_dash import input_tiker, button_enter

data1 = get_tinkoff_chart('SBER')
app = dash.Dash(__name__)

app.layout = html.Div( children=[
    html.Div(children=[
        html.Div(input_tiker),
        html.Div(button_enter)],
        style={"display": "grid", "grid-template-columns": "1fr 1fr",  "gap": "13px"}),
    # dbc.Input(id="input-1", type="str", placeholder="Введите тикер", valid=False, class_name="form-control is-valid", html_size=100),


    # dbc.Button("1m", id='time-frame1m', color="blue", size="lg", style={"font-size": "1.6rem"},className="me-md-2"),
    # dbc.Button("5m", id='time-frame5m', color="blue", size="lg", style={"font-size": "1.6rem"},className="me-md-2"),
    # dbc.Button("1h", id='time-frame30m', color="blue", size="lg", style={"font-size": "1.6rem"},className="me-md-2"),
    # dbc.Button("1d", id='time-frame1h', color="blue", size="lg", style={"font-size": "1.6rem"},className="me-md-2"),
    dash_tvlwc.Tvlwc(
        id='chart',
        seriesData=[data1],
        seriesTypes=['candlestick'],
        width= '100vw',
        height='700px',#'400px'

    )
])

buttons = html.Div(children=
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
    Output('input-tiker', 'placeholder'),
    Output('chart', 'seriesData'),
    Input("button-enter", 'n_clicks'),
    State("input-tiker", 'value'),
    prevent_initial_call=True
)
def on_button_click(n_clicks, value : str):
    print(value)
    if "/" in value:
        list_tikers = [i.strip() for i in value.split('/')]
        kol_tiker = len(list_tikers)
        # if kol_tiker == 2
        tikir1 = get_tinkoff_chart(list_tikers[0])
        tikir2 = get_tinkoff_chart(list_tikers[1])
        data = calculate_spread(tikir1, tikir2)
        placeholder_text = value.upper()
        if data:
            return placeholder_text, [data]
        else:
            return None
    else:
        data = get_tinkoff_chart(value)
        placeholder_text = value.upper()
        if data:
            return placeholder_text, [data]
        else:
            return None
    # return
# if __name__ == "__main__":
#     app.run_server(debug=True, host="0.0.0.0", port=8000)
