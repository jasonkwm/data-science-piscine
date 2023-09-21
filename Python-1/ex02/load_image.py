from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Load image base on path given
    print err if not cant load
    """
    try:
        assert isinstance(path, str), "path problem"
        img = Image.open(path)
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
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
