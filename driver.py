import argparse

import matplotlib.pyplot as plt
import skimage.io as skio
import numpy as np

from align import align_handler
from image import Image


def main(args):
    p1, p2 = args.path1, args.path2
    i1, i2 = Image(p1), Image(p2)

    i1.image = align_handler(i2.image, i1.image, 3, factor=0.025,
                             freeze_y=args.freeze_y, freeze_x=args.freeze_x)
    # np.roll(i1, (50,0), axis=(1,0))
    # i1.image = np.roll(i1.image, (20, 0), axis=(1, 0))
    if args.frequency:
        skio.imsave('/Users/mdt/projects/computational-photography-p2/images/results/anakin/i1_freq.png', np.log(np.abs(np.fft.fftshift(np.fft.fft2(i1.gray)))))
        skio.imsave('/Users/mdt/projects/computational-photography-p2/images/results/anakin/i2_freq.png', np.log(np.abs(np.fft.fftshift(np.fft.fft2(i2.gray)))))

    # else:
    f1 = i1.apply_filter('gaussian', (61, 61),
                        args.i1_sigma, args.i1_sigma, frequency='low')
    f2 = i2.apply_filter('gaussian', (61, 61),
                        args.i2_sigma, args.i2_sigma, frequency='high')
    # plt.imshow(f1+f2)
    skio.imsave('/Users/mdt/projects/computational-photography-p2/images/results/anakin/f1.png', f1)
    skio.imsave('/Users/mdt/projects/computational-photography-p2/images/results/anakin/f2.png', f2)

    # skio.imsave('/Users/mdt/projects/computational-photography-p2/images/results/palace/3_2.png', (f1+f2) )

    # plt.show()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Create hybrid Images!')
    parser.add_argument('--path1', help='path to image 1')
    parser.add_argument('--path2', help='path to image 2')
    parser.add_argument('--frequency', type=bool, default=False)
    parser.add_argument(
        '--freeze_x', help='freeze image alignment in x', type=bool, default=False)
    parser.add_argument(
        '--freeze_y', help='freeze image alignment in y', type=bool, default=False)
    parser.add_argument('--i1_sigma', help='sigma', type=float, default=3)
    parser.add_argument('--i2_sigma', help='sigma', type=float, default=3)

    args = parser.parse_args()
    main(args)
