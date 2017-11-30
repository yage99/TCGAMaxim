# -*- coding: utf-8 -*-

import sys
import time


# Print iterations progress
def printProgressBar(iteration, total, time_start=None, prefix='',
                     suffix='', decimals=1, length=50, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
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
