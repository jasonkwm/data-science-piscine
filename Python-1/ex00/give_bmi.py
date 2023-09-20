import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if (len(height) != len(weight)):
        raise ValueError("invalid lists")
    
    return np.divide(weight, np.multiply(height, height)).tolist()



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [ i < limit for i in bmi]
