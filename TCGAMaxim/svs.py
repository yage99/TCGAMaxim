import openslide
import os
from utils import printProgressBar


class svs:
    import re
    _matcher = re.compile("TCGA-\w{2}-\w{4}-\w{3}-\w{2}-\w{3}")

    def __init__(self, file):

        self.slide = openslide.OpenSlide(file)
        self.location, self.sourceFile = os.path.split(file)

    def slideWholeSlide(self, location, unit=1024):
        width, height = self.slide.dimensions

        slide_count = 0
        slide_start = [0, 0]

        allCount = ((width / unit + (width % unit != 0))
                    * (height / unit + (height % unit != 0)))

        id = svs._matcher.search(self.sourceFile).group()
        while slide_start[1] < height:
            while slide_start[0] < width:
                img = self.slide.read_region(slide_start, 0, (unit, unit))

                img.save(os.path.join(location,
                                      ("%s_%03d.png" % (id, slide_count))))

                slide_count = slide_count + 1
                slide_start[0] = slide_start[0] + unit

                printProgressBar(slide_count, allCount,
                                 prefix=("%s:" % id),
                                 length=30)

            slide_start[0] = 0
            slide_start[1] = slide_start[1] + unit

        print(id + " process finished")
