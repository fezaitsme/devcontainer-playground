"""module docstring"""


def lambda_handler(event, context):
    """Test"""
    print2(2.4)


def print2(what: str) -> None:
    """doc string"""
    print(what)


def time_two(number: int) -> int:
    """Times a number by two"""
    return number * 2
