import imp
from image import Image
import skimage.io as skio
import numpy as np
def main():
    p1, p2 = '/Users/mdt/projects/computational-photography-p2/images/cat_dog/cat_bigger.jpeg','/Users/mdt/projects/computational-photography-p2/images/cat_dog/dog_bigger.jpeg'

    i1, i2 = Image(p1), Image(p2)
    i1.image = np.roll(i1.image, (-100, 0), axis=(0,1))
    f1 = i1.apply_filter('gaussian', (101,101), 10, 10, frequency='low')
    f2 = i2.apply_filter('gaussian', (101,101), 9,9, frequency='high')
    # skio.imshow(np.concatenate((f1, f2), axis=1))
    skio.imsave('./images/results/cat_dog/cat_dog.png',f1 + f2)
    # print()

if __name__ == '__main__':
    main()