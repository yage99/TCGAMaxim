# -*- coding: utf-8 -*-
import os

class meta:
    import re
    _id_matcher = re.compile('TCGA-\w{2}-\w{4}')
    def __init__(self, file):
        self.file = file

        import csv

        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            header = reader.next()
            self.lines = []

            for line in reader:
                self.lines.append(line)

    def __iter__(self):
        return iter(self.lines)

    def files(self):
        for line in self.lines:
            #dic = {}
            
            #dic['id'] = meta._id_matcher.search(line[1]).group()
            #dic['file'] = line[0] + "/" + line[1]
            yield (meta._id_matcher.search(line[1]).group(), os.path.join(line[0], line[1]))
            

