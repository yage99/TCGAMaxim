# -*- coding: utf-8 -*-
import os


class meta:
    '''
    This class reads and provides convenient function for iterate files listed
    in the specified meta file.
    After initialization, one can use for...in structure to iterate (id, file)
    '''

    import re
    _id_matcher = re.compile('TCGA-\w{2}-\w{4}')

    def __init__(self, file):
        '''
        init function for the meta class
        '''
        self.file = file

        import csv

        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)
            self.lines = []

            for line in reader:
                self.lines.append(line)

    def __iter__(self):
        for line in self.lines:
            yield (meta._id_matcher.search(line[1]).group(),
                   os.path.join(line[0], line[1]))
        # return iter(self.lines)

    def __len__(self):
        return len(self.lines)

    def list(self):
        '''
        return the real list in the meta file
        '''
        return self.lines
