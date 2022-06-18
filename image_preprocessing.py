import cv2 as cv
from cv2 import INTER_AREA
from constants import *

import PIL.Image
import torchvision.transforms.functional as transform_functional
import torchvision.transforms.transforms
import torchvision.transforms as transforms

import numpy as np

# def downsample(img, downsample_ratio):
#     img = cv.imread(img)
#     shape = img.shape
#     cv.imshow("before", img)
#     # print(shape)
#     img = cv.resize(img, ((int)(shape[1]/downsample_ratio), (int)(shape[0]/downsample_ratio)), interpolation=cv.INTER_CUBIC)
#     cv.imshow("small", img)
#     # # img = img.resize(img[0]/2, img[1]/2)
#     # cv.imshow("small", img)
#     img = cv.resize(img, (shape[1], shape[0]), interpolation=cv.INTER_AREA)
#     cv.imshow("final", img)
#     cv.waitKey(0)

# if __name__ == "__main__":
#     downsample(example_dog)


def downsample_pytorch(img, downsample_ratio):

        img = transform_functional.resize(img, 
                ((int)(img.size[1]/downsample_ratio), 
                (int)(img.size[0]/downsample_ratio)), interpolation=torchvision.transforms.transforms.InterpolationMode.NEAREST)

        img = transform_functional.resize(img,
                ((int)(img.size[1]*downsample_ratio),
                (int)(img.size[0]*downsample_ratio)), interpolation=torchvision.transforms.transforms.InterpolationMode.NEAREST)


def normalising_windows(min, max, values):
        return (values-min)/((max-min)*1.0)

def windowing(img):
        img = np.array(img)
        max = (np.amax(np.amax(img, axis=1), axis=0))
        min = (np.amin(np.amin(img, axis=1), axis=0))

        print(img.shape)

        img = img - min
        img = img / (max - min)

        print(img)

        cv.imshow("img", img)
        cv.waitKey(0)

if __name__ == "__main__":
        IMG = image_109
        IMG = PIL.Image.open(IMG)
        # downsample_pytorch(IMG, 100)
        windowing(IMG)