import numpy as np
import skimage as sk
import skimage.io as skio

from filter import gaussian_filter


class Image:
    def __init__(self, path) -> None:
        self.image = sk.img_as_float32(skio.imread(path))

    def apply_filter(self, filter_type, filter_size, sigmax, sigmay, frequency='low'):
        if filter_type == 'gaussian':
            r, g, b = self.__get_color_channels()
            return self.__apply_gaussian((r, g, b), filter_size, sigmax, sigmay, frequency=frequency)

    def __apply_gaussian(self, image_channels, filter_size, sigmax, sigmay, frequency='low'):
        blurred_r = gaussian_filter(
            image_channels[0], filter_size, sigmax, sigmay)
        blurred_g = gaussian_filter(
            image_channels[1], filter_size, sigmax, sigmay)
        blurred_b = gaussian_filter(
            image_channels[2], filter_size, sigmax, sigmay)

        if frequency == 'low':
            return np.dstack([blurred_r, blurred_g, blurred_b])
        else:
            return np.dstack([image_channels[0]-blurred_r, image_channels[1]-blurred_g, image_channels[2]-blurred_b])

    def __get_color_channels(self):
        # R, G,B
        return self.image[:, :, 0], self.image[:, :, 1], self.image[:, :, 2]
