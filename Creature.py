from tensorflow.keras import models
from tensorflow.keras import layers
import numpy as np, tensorflow as tf
import uuid
# A creature describes a neural network
# This class creates a creature from a genome which describes the structure of the neural network
# the input and output layers are fixed. And the genomes specifies the arrangment of the hidden layers. 
class Creature():
    def __init__(self,genome):
        self.genome = genome
        self.id = uuid.uuid1()
        self.model = models.Sequential()

    def develop(self,input_shape):
        for gene in self.genome.genes:
            # if input layer
            if gene[0] == 0:
                self.model.add(layers.Dense(2**gene[1], 
                        activation = 'relu', 
                        input_shape = (input_shape, )))
            # if ouput layer
            elif gene[0] == 1:
                self.model.add(layers.Dense(1))
            else:
                self.model.add(layers.Dense(2**gene[1], activation = 'relu'))

            self.model.compile(optimizer = 'rmsprop', loss = 'mse', metrics = ['mae'])
    def __str__(self) -> str:
        return str(self.id)
    # def build_model():
    #     model = models.Sequential()
    #     model.add(layers.Dense(64, 
    #                         activation = 'relu', 
    #                         input_shape = (train_data.shape[1], )))
    #     model.add(layers.Dense(64, activation = 'relu'))
    #     model.add(layers.Dense(1))
    #     model.compile(optimizer = 'rmsprop', loss = 'mse', metrics = ['mae'])
    
    #     return model
