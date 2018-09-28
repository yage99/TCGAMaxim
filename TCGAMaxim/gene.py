import gzip

class gene:
    def __init__(self, file):
        self.file = file

        self.data = gzip.GzipFile(mode='rb', fileobj = open(file, 'rb'))
        
