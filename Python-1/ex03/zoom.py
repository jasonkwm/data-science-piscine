from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def zoomer(img, factor):
    """
    @params
    img: is a 3d numpy array
    factor: 0 to 1 on the factor u want to zoom in
    """
    try:
        assert factor > 0 and factor <= 1, "wrong factor"
        assert len(img.shape) > 1, "image problem"
        img_shape = img.shape
        h = round(img_shape[0] * factor)
        w = round(img_shape[1] * factor)
        hs = round((img_shape[0] - h) / 2)
        ws = round((img_shape[1] - w) / 2)
        zoom_img = img[hs:h + hs, ws:w + ws]
        grey_img = np.dot(zoom_img[..., :3], [0.2989, 0.5870, 0.1140])
        grey_img = grey_img.reshape(grey_img.shape[0], grey_img.shape[1], -1)
        grey_img = np.round(grey_img).astype(int)
        shape2 = grey_img.shape[:2]
        print(f"New shape after slicing: {grey_img.shape} or {shape2}")
        print(grey_img)
        plt.imshow(grey_img, cmap="gray")
        plt.show()
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
    except KeyboardInterrupt:
        pass


def main():
    """This is a main, By Odin, by Thor ! Use your brain !!!"""
    img = ft_load("./animal.jpeg")
    zoomer(img, 0.5)


if __name__ == "__main__":
    main()
