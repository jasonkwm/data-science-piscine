import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if (len(height) != len(weight)):
        raise ValueError("invalid lists")
    return list(np.divide(height, weight))



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    pass

print(give_bmi([20.0,50.0], [1.2,1.8]))