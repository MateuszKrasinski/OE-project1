import random

from chromosome import Chromosome

class Population:
    def __init__(self, bounds, chromosome_length, population_number, createPopul = True):
        self.size = population_number
        self.bounds = bounds
        self.chromosome_length = chromosome_length
        self.population= []
        if createPopul:
            self.population  = [Chromosome(chromosome_length, bounds) for _ in range(population_number)]

    def decodeAll(self):
        return [p.decode() for p in self.population]

    def scoreAll(self, desired_function):
        return [desired_function(p.decode()) for p in self.population]

    def create_next(self):
        return Population(self.bounds, self.chromosome_length, self.size, False)
