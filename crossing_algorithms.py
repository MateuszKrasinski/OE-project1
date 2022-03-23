
from abc import ABC, abstractmethod
from audioop import cross
from numpy.random import randint
from numpy.random import rand
from chromosome import Chromosome, ChromosomeList


class BaseCrossing(ABC):
    def __init__(self, cross_propability):
        self.cross_probability = cross_propability
        super().__init__()

    @abstractmethod
    def cross(self, parent1: Chromosome, parent2: Chromosome) -> ChromosomeList:
        pass


class SinglePointCrossing (BaseCrossing):
    def __init__(self, cross_probability):
        super().__init__(cross_probability)

    def cross(self, parent1: Chromosome, parent2: Chromosome) -> ChromosomeList:
        child1, child2 = parent1.copy(), parent2.copy()
        if rand() < self.cross_probability:
            cross_point = randint(1, parent1.chromosome_length)
            child1.bits = parent1.bits[:cross_point] + \
                parent2.bits[cross_point:]
            child2.bits = parent2.bits[:cross_point] + \
                parent1.bits[cross_point:]

        return [child1, child2]
