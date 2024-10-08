from tinkoff_get_func import get_tinkoff_chart, moex_all_tikers_info
import pandas as pd


def remove_suffix_from_keys(dict_list):
    return [{'time' : i['time'], 'open' : i['open_spread'], 'high' : i['high_spread'], 'low' : i['low_spread'], 'close' : i['close_spread']}for i in dict_list]




def calculate_spread(ticker1, ticker2):
    ticker1_df = pd.DataFrame(ticker1)
    ticker2_df = pd.DataFrame(ticker2)
    # Объединяем таблицы по времени
    df = pd.merge(ticker1_df, ticker2_df, on='time', suffixes=('_ticker1', '_ticker2'))

    # Создаем DataFrame для спреда
    spread_df = pd.DataFrame()
    spread_df['time'] = df['time']

    # Перечисляем все ключевые столбцы для деления
    keys = ['open', 'high', 'low', 'close']

    for key in keys:
        ticker1_col = f'{key}_ticker1'
        ticker2_col = f'{key}_ticker2'
        spread_col = f'{key}_spread'

        # Выполняем деление и сохраняем результат в новый столбец
        spread_df[spread_col] = df[ticker1_col] / df[ticker2_col]
    # print(spread_df)
    data = spread_df.to_dict('records')
    nev_data = remove_suffix_from_keys(data)
    return nev_data
# akc1 = pd.DataFrame(get_sandels_day("SBER"))
# akc2 = pd.DataFrame(get_sandels_day("GAZP"))
# calculate_spread(akc2, akc1)

def spread_2_delitela(tiker_list  : list):
    tiker1 = tiker_list[0]
    tiker2 = tiker_list[1]
    if tiker1 in moex_all_tikers_info.keys() and tiker2 in moex_all_tikers_info.keys():
        chart_tiker1 = get_tinkoff_chart(tiker1)
        chart_tiker2 = get_tinkoff_chart(tiker2)
        spread_chart = calculate_spread(chart_tiker1, chart_tiker2)
        placeholder_text = f"{tiker1}/{tiker2}"
        new_prefix_url = f"{tiker1.lower()}:{tiker2.lower()}"
        return placeholder_text, [spread_chart], new_prefix_url
    else:
        return False


def spread_3_delitela(tiker_list  : list):
    tiker1 = tiker_list[0]
    tiker2 = tiker_list[1]
    tiker3 = tiker_list[2]
    if tiker1 in moex_all_tikers_info.keys() and tiker2 in moex_all_tikers_info.keys():
        chart_tiker1 = get_tinkoff_chart(tiker1)
        chart_tiker2 = get_tinkoff_chart(tiker2)
        chart_tiker3 = get_tinkoff_chart(tiker3)
        spread_chart1 = calculate_spread(chart_tiker1, chart_tiker2)
        spread_chart2 = calculate_spread(spread_chart1, chart_tiker3)
        placeholder_text = f"{tiker1}/{tiker2}/{tiker3}"
        new_prefix_url = f"{tiker1.lower()}:{tiker2.lower()}:{tiker3.lower()}"
        return placeholder_text, [spread_chart2], new_prefix_url
    else:
        return False
