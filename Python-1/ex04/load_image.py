from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Different from previous load image
    does not contain print
    """
    try:
        assert isinstance(path, str), "path problem"
        img = Image.open(path)
        img_array = np.array(img)
        return img_array
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
        return np.array([])
    except FileNotFoundError:
        print("Error: file not found")
        return np.array([])
    except UnidentifiedImageError:
        print("Error: file not image")
        return np.array([])
    except PermissionError:
        print("Error: file problem")
        return np.array([])
