import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:
    """
    shift image to specific color tone
    """
    try:
        assert (isinstance(array, np.ndarray)), "array error"
        assert (array.ndim == 3), "array problem"
        temp = 255 - array
        print(f"The shape of image is: {temp.shape}")
        print("Inverts the color of the image received.")
        plt.imshow(temp)
        plt.show()
        return temp
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))


def ft_red(array) -> np.array:
    """
    shift image to specific color tone
    """
    try:
        assert (isinstance(array, np.ndarray)), "array error"
        assert (array.ndim == 3), "array problem"
        temp = array * [1, 0, 0]
        print(f"The shape of image is: {temp.shape}")
        print("Reds the color of the image received.")
        plt.imshow(temp)
        plt.show()
        return temp
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))


def ft_green(array) -> np.array:
    """
    shift image to specific color tone
    """
    try:
        assert (isinstance(array, np.ndarray)), "array error"
        assert (array.ndim == 3), "array problem"
        temp = array * [0, 1, 0]
        print(f"The shape of image is: {temp.shape}")
        print("Greens the color of the image received.")
        plt.imshow(temp)
        plt.show()
        return temp
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))


def ft_blue(array) -> np.array:
    """
    shift image to specific color tone
    """
    try:
        assert (isinstance(array, np.ndarray)), "array error"
        assert (array.ndim == 3), "array problem"
        temp = array * [0, 0, 1]
        print(f"The shape of image is: {temp.shape}")
        print("Blues the color of the image received.")
        plt.imshow(temp)
        plt.show()
        return temp
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))


def ft_grey(array) -> np.array:
    """
    shift image to specific color tone
    """
    try:
        assert (isinstance(array, np.ndarray)), "array error"
        assert (array.ndim == 3), "array problem"
        temp = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
        temp = temp.reshape(temp.shape[0], temp.shape[1], -1)
        print(f"The shape of image is: {temp.shape}")
        print("Greys the color of the image received.")
        plt.imshow(temp, cmap="gray")
        plt.show()
        return temp
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
