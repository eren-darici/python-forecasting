from pandas._config.config import reset_option
from time_series.stationary_series import exponential_smoothing, moving_averages
import pandas as pd


def test_exponential_smoothing(demands):
    pass


def test_moving_averages(demands):
    return moving_averages(demands, 3)


if __name__ == '__main__':
    test_demands = pd.Series([1500.0, 2200.0, 2700.0, 4200.0, 7800.0, 5400.0])

    assert test_moving_averages(
        test_demands) == 3033.3333333333335, "Should be 3033.3333333333335"

    print("Everything passed")
