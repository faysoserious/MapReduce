# -*- coding: utf-8 -*-


from mrjob.job import MRJob

import re

WORD_RE = re.compile(r"[\w']+")


class MRWordOccurrences(MRJob):



    def mapper(self, _, line):
        # yield each word in the line
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)
    
    def reducer(self, word, counts):
        # send all (num_occurrences, word) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        yield (word,sum(counts))


if __name__ == '__main__':
    MRWordOccurrences.run()
