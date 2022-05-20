
# A genome describes the structure of a neural network
# A gene describes a single layer in the neural network.
# A gene consists of two numbers. 
# The first number specifies the type of the layer, 
# the second number specifies the number of units.
import Environment
import random
import Creature
class Genome():
    def __init__(self,num_of_genes=4):
        if(num_of_genes < 2):
            raise Exception('Num of Genes must be greature than 2')
        self.genes = [[3,random.randint(3,7),random.randint(0,1)] for i in range(num_of_genes-2)]
        self.genes.append([1,0])
        self.genes.insert(0,[0,random.randint(3,7)])


