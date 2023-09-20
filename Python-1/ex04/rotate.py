from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def squarer_n_grayer(img, factor):
    img_shape = img.shape
    dim = img_shape[0] if img_shape[0] < img_shape[1]\
        else img_shape[1]
    square = round(dim * factor)
    start = round((dim - square) / 2)
    square_img = img[start:start + square, start:start + square]
    grey_img = np.dot(square_img[..., :3], [0.2989, 0.5870, 0.1140])
    channel = grey_img.shape + (1,)
    print(f"The shape of image is: {channel} or {grey_img.shape}")
    print(grey_img)
    return grey_img


def rotater(img, factor):
    """
    @params
    img: is a 3d numpy array
    factor: 0 to 1 on the factor u want to zoom in
    """
    try:
        assert factor > 0 and factor <= 1, "wrong factor"
        assert len(img.shape) > 1, "image problem"
        square_img = squarer_n_grayer(img, factor)
        rotate_img = np.transpose(square_img)
        print(f"New shape after Transpose: {rotate_img.shape}")
        print(rotate_img)
        plt.imshow(rotate_img, cmap="gray")
        plt.show()
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))


def main():
    """This is a main, By Odin, by Thor ! Use your brain !!!"""
    img = ft_load("./animal.jpeg")
    rotater(img, 0.5)


if __name__ == "__main__":
    main()
