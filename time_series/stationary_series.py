import pandas as pd
import numpy as np


pd.set_option('mode.chained_assignment', None)


def exponential_smoothing(demand_col: pd.Series, alpha: float):
    """
    returns exponential smoothing for given alpha
    """

    demand_plus = list(demand_col.copy())
    demand_plus.append(None)

    new_dataframe = pd.DataFrame({'demand': demand_plus,
                                  'forecast': [None for _ in range(len(demand_plus))]})

    new_dataframe.forecast[0] = float(demand_col[0])

    for i in range(1, len(demand_plus)):
        new_dataframe.forecast[i] = new_dataframe.demand[i-1] * \
            alpha + new_dataframe.forecast[i-1] * (1-alpha)

    return new_dataframe


def moving_averages(dataframe_col: pd.Series, n: int):
    """
    returns moving average for n 
    """
    sum = 0

    try:
        for i in range(n):
            sum += dataframe_col[n-i]
        return sum / n
    except Exception as e:
        return e
