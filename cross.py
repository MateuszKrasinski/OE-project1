from numpy.random import randint
from numpy.random import rand

import chromosome
from population import Population


class Cross:
    def __init__(self, cross_probability):
        self.cross_probability = cross_probability

    def cross(self, parent1, parent2):
        child1, child2 = parent1.copy(), parent2.copy()
        if rand() < self.cross_probability:
            cross_point = randint(1, parent1.chromosome_length)
            child1.bits = parent1.bits[:cross_point] + parent2.bits[cross_point:]
            child2.bits = parent2.bits[:cross_point] + parent1.bits[cross_point:]

        return [child1, child2]