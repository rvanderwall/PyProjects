from math import isclose, sqrt


class LengthException(Exception):
    def __init__(self, expected, actual):
        super().__init__(f"Invalid basis vector length, is {actual} but should be {expected}")


def get_length(v:list):
    len = 0
    for x in v:
        len += x * x
    len = sqrt(len)
    return len


def normalize(v:list):
    len = get_length(v)
    return [vv / len for vv in v]


def check_length(v):
    len = get_length(v)
    if not isclose(len, 1.0, rel_tol=1e-3, abs_tol=0.0):
        e = LengthException(1.0, len)
        raise e
