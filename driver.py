import argparse

import skimage.io as skio

from align import align_handler
from image import Image


def main(args):
    p1, p2 = args.path1, args.path2
    i1, i2 = Image(p1), Image(p2)

    # i1.image = np.roll(i1.image, (-100, 0), axis=(0,1))
    i1.image = align_handler(i2.image, i1.image, 3, factor=0.12,
                             freeze_y=args.freeze_y, freeze_x=args.freeze_x)
    f1 = i1.apply_filter('gaussian', (101, 101),
                         args.i1_sigma, args.i1_sigma, frequency='low')
    f2 = i2.apply_filter('gaussian', (101, 101),
                         args.i2_sigma, args.i2_sigma, frequency='high')
    # skio.imshow(np.concatenate((f1, f2), axis=1))
    skio.imsave(
        './images/results/cat_dog/cat_dog_auto_align_mean.png', (f1 + f2) / 2)
    # print()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--path1', help='path to image 1')
    parser.add_argument('--path2', help='path to image 2')
    parser.add_argument(
        '--freeze_x', help='freeze image alignment in x', type=bool, default=False)
    parser.add_argument(
        '--freeze_y', help='freeze image alignment in y', type=bool, default=False)
    parser.add_argument('--i1_sigma', help='sigma', type=int, default=3)
    parser.add_argument('--i2_sigma', help='sigma', type=int, default=3)

    args = parser.parse_args()
    main(args)
