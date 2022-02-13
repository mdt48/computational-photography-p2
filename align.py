import cv2
import numpy as np
import skimage as sk

from filter import gaussian_filter


def sobel_edge_detection(img_blur):
    # Combined X and Y Sobel Edge Detection
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
    return sobelxy


def preprocess(img):
    # grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blur
    blurred = gaussian_filter(gray, (3, 3), 0, 0)

    edges = sobel_edge_detection(blurred)
    return edges


def pyramids(img, height=4):
    """
    Takes in the three color channels and downsamples by half height times.
    Returns dictionary of the pyramid downsampling
    """
    pyramids = []
    for i in range(height-1, -1, -1):
        factor = 0.5**i
        pyramids.append(cv2.resize(img, (0, 0), fx=factor, fy=factor))

    return pyramids


def sse(i1, i2):
    return np.sum(np.square(i2 - i1))


def align(img1, img2, displacement_size, freeze_x=False, freeze_y=False):
    sses = []
    displacements = []
    for x in range(-displacement_size, displacement_size):
        if freeze_x and x != 0:
            continue
        for y in range(-displacement_size, displacement_size):
            if freeze_y and y != 0:
                continue
            displaced_i2 = np.roll(img2, (x, y), axis=(1, 0))

            sses.append(sse(img1, displaced_i2))
            displacements.append((x, y))

    best_idx = np.argmin(sses)

    return displacements[best_idx]


def align_handler(img1, img2, pyramid_height, factor, freeze_x=False, freeze_y=False):
    edges1 = preprocess(img1)
    edges2 = preprocess(img2)

    pyramid1 = pyramids(edges1, height=pyramid_height)
    pyramid2 = pyramids(edges2, height=pyramid_height)

    dy, dx = 0, 0
    for i in range(pyramid_height):
        displacement_size = int(
            factor*pyramid1[pyramid_height-1].shape[0]) if i == 0 else 2

        disp = align(pyramid1[i], pyramid2[i], displacement_size,
                     freeze_y=freeze_y, freeze_x=freeze_x)
        dx += disp[0]*2
        dy += disp[1]*2
    print(dx, dy)
    aligned_i2 = np.roll(img2, (dx, dy), axis=(1, 0))
    return aligned_i2
