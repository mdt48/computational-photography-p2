import cv2 as cv


def gaussian_filter(image, size: tuple, sigma_x, sigma_y):
    return cv.GaussianBlur(image, size, sigmaX=sigma_x, sigmaY=sigma_y)
