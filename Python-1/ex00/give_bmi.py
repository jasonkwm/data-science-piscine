import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
            -> list[int | float]:
    try:
        assert len(height) == len(weight), "wrong list length"
        assert np.issubdtype(np.array(weight).dtype, np.number), "wrong type"
        assert np.issubdtype(np.array(height).dtype, np.number), "wrong type"
        return np.divide(weight, np.multiply(height, height)).tolist()
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        assert np.issubdtype(np.array(bmi).dtype, np.number), "wrong type"
        assert isinstance(limit, int), "wrong type"
        return [i < limit for i in bmi]
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
        return []
