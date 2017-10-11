# -*- coding: utf-8 -*-

from svs import svs
from threading import Thread
from meta import meta
import os
import sys
import multiprocessing as mp
from utils import printProgressBar

allFilesCount = 0
currentFileProcessed = 0

def log_callback(result):
    global currentFileProcessed, allFilesCount
    currentFileProcessed = currentFileProcessed + 1
    print("Overall Progressing: %d/%d" % (currentFileProcessed, allFilesCount))
    printProgressBar(currentFileProcessed, allFilesCount,
                     prefix = ("%d/%d:"),
                     length = 30)

def process(location, svsFile):
    slide = svs(os.path.join(location, svsFile))

    #thread = Thread(target = slide.slideWholeSlide,
    #         args = (slide.location, 1024,))
    #pool.apply_async(slide.slideWholeSlide,
    #                 args = (slide.location, 1024, ),
    #                 callback = log_callback)
    slide.slideWholeSlide("/media/af214dbe-b6fa-4f5e-932a-14b133ba4766/zhangya/svs-processed", 1024)
        

def main(metaFile):
    global allFilesCount
    svsSlides = meta(metaFile)
    location, filename = os.path.split(metaFile)
    print location

    pool = mp.Pool(20)

    for id, svsFile in svsSlides.files():
        print svsFile
        pool.apply_async(process, (location, svsFile, ),
                         callback = log_callback)
        
        allFilesCount = allFilesCount + 1

        #thread.start()
        #thread.join()
        #threads.append(thread)

    pool.close()
    pool.join()

    #for thread in threads:
    #    thread.join()

if __name__ == '__main__':
    #print sys.argv
    main(sys.argv[1])

