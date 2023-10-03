from src.lambda_handler import time_two


def test_times_two():
    assert time_two(5) == 10
