# -*- coding: utf-8 -*-

import sys
import time
import numpy as np


def rgb2lab(input_image):
    """
    rgb2lab function based on codes from
    https://stackoverflow.com/questions/13405956/convert-an-image-rgb-lab-with-python
    """
    xyz = np.zeros(input_image.shape)

    input_image = np.where(
            input_image > 0.04045,
            ((input_image + 0.055) / 1.055) ** 2.4,
            input_image / 12.92)

    input_image = input_image * 100

    xyz[:, :, 0] = (input_image[:, :, 0] * 0.4124 +
                    input_image[:, :, 1] * 0.3576 +
                    input_image[:, :, 2] * 0.1805)
    xyz[:, :, 1] = (input_image[:, :, 0] * 0.2126 +
                    input_image[:, :, 1] * 0.7152 +
                    input_image[:, :, 2] * 0.0722)
    xyz[:, :, 2] = (input_image[:, :, 0] * 0.0193 +
                    input_image[:, :, 1] * 0.1192 +
                    input_image[:, :, 2] * 0.9505)
    xyz = np.round(xyz, 4)

    xyz[:, :, 0] = xyz[:, :, 0] / 95.047
    xyz[:, :, 1] = xyz[:, :, 1] / 100.0
    xyz[:, :, 2] = xyz[:, :, 2] / 108.883

    xyz = np.where(
            xyz > 0.008856,
            xyz ** (0.3333333333333333),
            7.787 * xyz + 16 / 116)

    lab = np.zeros(xyz.shape)
    lab[:, :, 0] = 116 * xyz[:, :, 1] - 16
    lab[:, :, 1] = 500 * (xyz[:, :, 0] - xyz[:, :, 1])
    lab[:, :, 2] = 300 * (xyz[:, :, 1] - xyz[:, :, 2])

    # L = ( 116 * XYZ[ 1 ] ) - 16
    # a = 500 * ( XYZ[ 0 ] - XYZ[ 1 ] )
    # b = 200 * ( XYZ[ 1 ] - XYZ[ 2 ] )

    lab = np.round(lab, 4)

    return lab


# Print iterations progress
def printProgressBar(iteration, total, time_start=None, prefix='',
                     suffix='', decimals=1, length=30, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        time_start  - Optional  : start time of process (Long)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in
                                  percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals)
               + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    left_time_str = ""
    if time_start is not None and iteration != 0:
        current_time = time.time()
        left_time = ((current_time - time_start)
                     / float(iteration) * (total - iteration))
        left_time_str = ("%02d:%02d:%02d"
                         % (int(left_time / 3600),
                            int((left_time % 3600) / 60),
                            int(left_time % 60)))
    sys.stdout.write('\r%s (%d/%d)|%s| %s%% %s %s'
                     % (prefix, iteration, total, bar,
                        percent, suffix, left_time_str))
    sys.stdout.flush()
    # Print New Line on Complete
    if iteration == total:
        print()
