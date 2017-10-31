# -*- coding: utf-8 -*-

from mrjob.job import MRJob
from mrjob.step import MRStep
import re
GRAPH_RE = re.compile(r"[\d']+")

class MRMostUsedWord(MRJob):
    def mapper_get_nodes(self, _, line):
        # yield each nodes in the line
        for node in GRAPH_RE.findall((line)):
#            print("(node{},1)".format(node))
            print('%s\t%s' % (node, 1))
            yield (node, 1)

    #def combiner_count_nodes(self, node, counts):
        # sum the nodes we've seen so far
    #    yield (node, sum(counts))
    
    def reducer_nodes_degree(self, node, counts):
        # send all (degree, nodes) pairs to the same reducer.
#        print(node,sum(counts))
        yield node,sum(counts)
#       yield None,(sum(counts),node)
       

        

    # discard the key; it is just None
    def determine_euler_tour(self,node,degree):
        # each item of word_count_pairs is (degree, nodes),
        # so yielding one results in key=counts, value=word
       for value in degree:
           
            if (value%2!=0):
                yield ('odd',1)
            else:
                yield ('even',1)
#                print('The degree of node{} is NOT even'.format(node)) 
     
#                print('The Degree of node{} is even'.format(node))
    def euler_tour(self,node,degree):
        print('\n--------------------------------------\n')
        if (node=='odd'):
            print('The graph has NOT an Euler tour')
            
        else:
            print('The graph has an Euler Tour')
        print('--------------------------------------\n')

            

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_nodes,
#                   combiner=self.combiner_count_nodes,
#                    reducer_init = self.reduce_init,
                   reducer=self.reducer_nodes_degree)
            ,MRStep(
                   
                   reducer=self.determine_euler_tour
                   )
             ,MRStep(
                   
                   reducer=self.reducer_nodes_degree
                   )
              ,MRStep(
                   
                   reducer=self.euler_tour
                   )
        ]

if __name__ == '__main__':
    MRMostUsedWord.run()
    
