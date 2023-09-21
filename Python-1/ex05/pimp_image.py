import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:
    """
    Inverts the color of the image received.
    """
    try:
        assert (isinstance(array, np.ndarray)), "array error"
        assert (array.ndim == 3), "array problem"
        temp = 255 - array
        print(f"The shape of image is: {array.shape}")
        print(array)
        plt.imshow(temp)
        plt.show()
        return temp
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
    except KeyboardInterrupt:
        pass


def ft_red(array) -> np.array:
    """
    Reds the color of the image received.
    """
    try:
        assert (isinstance(array, np.ndarray)), "array error"
        assert (array.ndim == 3), "array problem"
        new_arr = np.empty(array.shape)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                new_arr[i, j, 0] = array[i, j, 0]
                new_arr[i, j, 1] = 0
                new_arr[i, j, 2] = 0
        new_arr = new_arr.astype(int)
        print(f"The shape of image is: {array.shape}")
        print(array)
        plt.imshow(new_arr)
        plt.show()
        return new_arr
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
    except KeyboardInterrupt:
        pass


def ft_green(array) -> np.array:
    """
    Greens the color of the image received.
    """
    try:
        assert (isinstance(array, np.ndarray)), "array error"
        assert (array.ndim == 3), "array problem"
        new_arr = np.empty(array.shape)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                new_arr[i, j, 0] = 0
                new_arr[i, j, 1] = array[i, j, 1]
                new_arr[i, j, 2] = 0
        new_arr = new_arr.astype(int)
        print(f"The shape of image is: {array.shape}")
        print(array)
        plt.imshow(new_arr)
        plt.show()
        return new_arr
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
    except KeyboardInterrupt:
        pass


def ft_blue(array) -> np.array:
    """
    Blues the color of the image received.
    """
    try:
        assert (isinstance(array, np.ndarray)), "array error"
        assert (array.ndim == 3), "array problem"
        new_arr = np.empty(array.shape)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                new_arr[i, j, 0] = 0
                new_arr[i, j, 1] = 0
                new_arr[i, j, 2] = array[i, j, 2]
        new_arr = new_arr.astype(int)
        print(f"The shape of image is: {array.shape}")
        print(array)
        plt.imshow(new_arr)
        plt.show()
        return new_arr
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
    except KeyboardInterrupt:
        pass


def ft_grey(array) -> np.array:
    """
    Greys the color of the image received.
    """
    try:
        assert (isinstance(array, np.ndarray)), "array error"
        assert (array.ndim == 3), "array problem"
        # grey_val = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
        # grey_val = grey_val.reshape(grey_val.shape[0], grey_val.shape[1], -1)
        grey_val = np.empty(array.shape[:2] + (1,))
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                r, g, b = array[i, j, 0], array[i, j, 1], array[i, j, 2]
                temp = r if r > g else g
                temp = temp if temp > b else b
                grey_val[i, j, 0] = temp
        grey_val = grey_val.astype(int)
        print(f"The shape of image is: {array.shape}")
        print(array)
        plt.imshow(grey_val, cmap="gray")
        plt.show()
        return grey_val
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
    except KeyboardInterrupt:
        pass
