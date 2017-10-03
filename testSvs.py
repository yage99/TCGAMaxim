from svs import svs
from threading import Thread

slide = svs('/Users/zhangya/Downloads/ffe47c76-056e-48a7-b184-938df6e703e9/TCGA-02-0054-01A-01-TS1.e362807e-460b-490f-9a29-2544ba144893.svs')
slide1 = svs('/Users/zhangya/Downloads/ffe47c76-056e-48a7-b184-938df6e703e9/TCGA-03-0054-01A-01-TS1.e362807e-460b-490f-9a29-2544ba144893.svs')
thread1 = Thread(target = slide.slideWholeSlide,
                 args = ("/Users/zhangya/Downloads/ffe47c76-056e-48a7-b184-938df6e703e9/",))
thread2 = Thread(target = slide1.slideWholeSlide,
                 args = ("/Users/zhangya/Downloads/ffe47c76-056e-48a7-b184-938df6e703e9/",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
    

