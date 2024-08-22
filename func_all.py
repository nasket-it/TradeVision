from tinkoff_get_func import get_tinkoff_chart
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