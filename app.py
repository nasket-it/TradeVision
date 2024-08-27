import dash
import aiohttp
import asyncio
# from flask import Flask, request
from func_all import spread_2_delitela, spread_3_delitela
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, State, no_update
from dash.dependencies import Input, Output
import dash_tvlwc
from  tinkoff_get_func import get_tinkoff_chart, moex_all_tikers_info
from elements_html_dash import input_tiker, button_enter, button_1d, button_1h, button_1m
from fastapi import FastAPI

# # Создаем приложение FastAPI
# app1 = FastAPI()
#
# # Создаем приложение Dash
# app = Dash(__name__, routes_pathname_prefix="/dash/")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



data1 = get_tinkoff_chart('SBER')



html.Div('ПРивет')
app.layout = html.Div(children=[
    dcc.Location(id='url-location', refresh=False),
    html.Div(children=[
        html.Div(input_tiker, style={"width": "100%"}),
        html.Div(children=[button_enter, button_1m, button_1h, button_1d], style={"width": "100%"}), ],
        style={"display": "grid", "grid-template-columns": "1fr 1fr",  "gap": "13px",
               'margin-bottom' : 20, 'margin-top' : 20 }),

    html.Div(dash_tvlwc.Tvlwc(
        id='chart',
        seriesData=[data1],
        seriesTypes=['candlestick'],
        width= 'auto',
        height='600px',#'400px'
    ), style={'margin-bottom' : 5, 'margin-right' : 5, 'margin-left' : 5 })

], style={
    'margin' : 'auto'
})


@app.callback(
    Output('input-tiker', 'placeholder'),
    Output('chart', 'seriesData'),
    Output('url-location', 'pathname'),
    Input("button-enter", 'n_clicks'),
    Input('url-location', 'pathname'),
    State("input-tiker", 'value'),
    prevent_initial_call=True
)
def on_button_click(n_clicks, pathname : str, value: str):
    print(87654, pathname)
    new_pathname = pathname.replace('/', '').strip().upper() if pathname != '/' else pathname
    if value:
        print(value)
        if "/" in value:
            list_tikers = [i.strip().upper() for i in value.split('/')]
            kol_tiker = len(list_tikers)
            if kol_tiker == 2:
                result = spread_2_delitela(list_tikers)
                if result:
                    return result
                else:
                    return no_update , no_update, no_update
            elif kol_tiker == 3:
                result = spread_3_delitela(list_tikers)
                if result:
                    return result
                else:
                    return no_update , no_update, no_update
            else:
                return no_update, no_update, no_update

        else:
            tiker = value.upper()
            if tiker in moex_all_tikers_info.keys():
                spread_chart = get_tinkoff_chart(tiker)
                placeholder_text = tiker
                new_prefix_url = tiker
                return placeholder_text, [spread_chart], new_prefix_url
            else:
                return no_update, no_update, no_update
    else:
        if new_pathname == '/' :
            print(8989898998)
            data = data1
            placeholder_text = 'SBER'
            new_prefix_url = '/sber'
            return placeholder_text,  [data], new_prefix_url
        elif new_pathname in moex_all_tikers_info.keys() :
            print(new_pathname)
            data = get_tinkoff_chart(new_pathname)
            placeholder_text = new_pathname
            new_prefix_url = new_pathname.lower()
            return placeholder_text, [data], new_prefix_url
        elif ':' in new_pathname:
            new_pathname = new_pathname.replace(":", "/")
            list_tikers = [i.strip().upper() for i in new_pathname.split('/')]
            kol_tiker = len(list_tikers)
            if kol_tiker == 2:
                result = spread_2_delitela(list_tikers)
                if result:
                    return result
                else:
                    return no_update, no_update, no_update
        else:
            return no_update, no_update, no_update



#-----------------------------------------------------------------------------------------------------
            # # if kol_tiker == 2:
            # tikir1 = get_tinkoff_chart(list_tikers[0])
            # tikir2 = get_tinkoff_chart(list_tikers[1])
            # data = calculate_spread(tikir1, tikir2)
            # placeholder_text = value.upper()
            # new_prefix_url = value.lower()


    # if value:
    #     # print(value)
    #     if "/" in value:
    #         list_tikers = [i.strip() for i in value.split('/')]
    #         kol_tiker = len(list_tikers)
    #         # if kol_tiker == 2:
    #         tikir1 = get_tinkoff_chart(list_tikers[0])
    #         tikir2 = get_tinkoff_chart(list_tikers[1])
    #         data = calculate_spread(tikir1, tikir2)
    #         placeholder_text = value.upper()
    #         new_prefix_url = value.lower()
    #
    #
    #         if data:
    #             return    placeholder_text, new_prefix_url, [data]
    #         else:
    #             return None
    #     else:
    #         data = get_tinkoff_chart(value)
    #         placeholder_text = value.upper()
    #         new_prefix_url = value.lower()
    #         if data:
    #             return placeholder_text, [data],new_prefix_url
    #         else:
    #             return None
    # else:
    #     data = get_tinkoff_chart(pathname[0].split('/')[0]) if pathname[0] in moex_all_tikers_info.keys() else data1
    #     placeholder_text = pathname[0].upper() if pathname[0] in moex_all_tikers_info.keys()  else 'SBER'
    #     new_prefix_url = pathname[0].lower() if pathname[0] in moex_all_tikers_info.keys()  else '/sber'
    #     return new_prefix_url, placeholder_text, [data]


# @app.callback(
#     Output('chart', 'seriesData'),
#     Input('url-location', 'pathname')  # Track the URL pathname
# )
# def update_chart(pathname):
#     # print(8765)
#     # Extract the ticker from the URL (e.g., '/GAZP' -> 'GAZP')
#     ticker = pathname.strip('/').upper()
#     print(ticker)
    # data1 = get_tinkoff_chart(ticker)
    # return data1
    # Get the data for the ticker
        # data = get_tinkoff_chart(ticker)

    # return
# if __name__ == "__main__":
#     app.run_server(debug=True, host="0.0.0.0", port=8000)

# import dash
# import aiohttp
# import asyncio
# import dash_bootstrap_components as dbc
# from dash import Dash, html, dcc, Input, Output, State
# import dash_tvlwc
# from tinkoff_get_func import get_tinkoff_chart, moex_all_tikers_info
# from elements_html_dash import input_tiker, button_enter, button_1d, button_1h, button_1m
# from func_all import calculate_spread
#
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# data1 = get_tinkoff_chart('SBER')
#
# app.layout = dbc.Container([
#     dcc.Location(id='url-location', refresh=False),
#
#     dbc.Row([
#         dbc.Col(input_tiker, xs=12, sm=12, md=6, lg=6, xl=6),
#         dbc.Col(button_enter, xs=12, sm=12, md=3, lg=3, xl=3),# Половина ширины на больших экранах
#     ], className="mb-3"),  # Добавляем отступ снизу
#
#     dbc.Row(
#         html.Div([
#         dbc.Col(button_1m,  className="mb-2"),
#         dbc.Col(button_1h,  className="mb-2"),
#         dbc.Col(button_1d,  className="mb-2"),
#         ],style={"width": "60%"})
#         ,className="mb-4"
#         ),  # Центрирование кнопок
#
#     dbc.Row([
#         dbc.Col(dash_tvlwc.Tvlwc(
#             id='chart',
#             seriesData=[data1],
#             seriesTypes=['candlestick'],
#             width='100%',  # Занимает всю ширину экрана
#             height='60vh',  # Высота в процентах от высоты экрана
#         ), xs=12, sm=12, md=12, lg=10, xl=10),  # График занимает 10/12 ширины на больших экранах
#     ], className="mb-4", style={'margin-left': 'auto', 'margin-right': 'auto'}),
#
# ], style={
#     'max-width': '100%',  # Максимальная ширина 100%
#     'margin': 'auto'  # Центрирование контента
# })
#
#
# @app.callback(
#     Output('input-tiker', 'placeholder'),
#     Output('chart', 'seriesData'),
#     Output('url-location', 'pathname'),
#     Input("button-enter", 'n_clicks'),
#     Input('url-location', 'pathname'),
#     State("input-tiker", 'value'),
#     prevent_initial_call=True
# )
# def on_button_click(n_clicks, pathname: str, value: str):
#     new_pathname = pathname.replace('/', '').strip().upper() if pathname != '/' else pathname
#     if new_pathname == '/' and value is None:
#         data = data1
#         placeholder_text = 'SBER'
#         new_prefix_url = '/sber'
#         return placeholder_text, [data], new_prefix_url
#     elif new_pathname in moex_all_tikers_info.keys() and value is None:
#         data = get_tinkoff_chart(new_pathname)
#         placeholder_text = new_pathname
#         new_prefix_url = new_pathname.lower()
#         return placeholder_text, [data], new_prefix_url
#     elif value:
#         if "/" in value:
#             list_tikers = [i.strip().upper() for i in value.split('/')]
#             kol_tiker = len(list_tikers)
#             if kol_tiker == 2:
#                 tiker1 = list_tikers[0]
#                 tiker2 = list_tikers[1]
#                 if tiker1 in moex_all_tikers_info.keys() and tiker2 in moex_all_tikers_info.keys():
#                     chart_tiker1 = get_tinkoff_chart(tiker1)
#                     chart_tiker2 = get_tinkoff_chart(tiker2)
#                     spread_chart = calculate_spread(chart_tiker1, chart_tiker2)
#                     placeholder_text = f"{tiker1}/{tiker2}"
#                     new_prefix_url = f"{tiker1.lower()}|{tiker2.lower()}"
#                     return placeholder_text, [spread_chart], new_prefix_url
#         else:
#             tiker = value.upper()
#             if tiker in moex_all_tikers_info.keys():
#                 spread_chart = get_tinkoff_chart(tiker)
#                 placeholder_text = tiker
#                 new_prefix_url = tiker
#                 return placeholder_text, [spread_chart], new_prefix_url
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
