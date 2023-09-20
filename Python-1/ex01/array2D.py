import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert isinstance(family, list), "Expected list"
        assert isinstance(start, int), "Start has to be int"
        assert isinstance(end, int), "End has to be int"
        nd_2d = np.array(family)
        assert len(nd_2d.shape) == 2, "Incomplete list"
        new_2d = nd_2d[start:end]
        print(f"My shape is : {nd_2d.shape}")
        print(f"My new shape is : {new_2d.shape}")
        return new_2d.tolist()
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
        return []
