
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

class DoublePointCrossing (BaseCrossing):
    def __init__(self, cross_probability):
        super().__init__(cross_probability)

    def cross(self, parent1: Chromosome, parent2: Chromosome) -> ChromosomeList:
        child1, child2 = parent1.copy(), parent2.copy()
        if rand() < self.cross_probability:
            cross_point1 = randint(1, parent1.chromosome_length)
            cross_point2 = randint(cross_point1, parent1.chromosome_length)
            child1.bits = parent1[:cross_point1] + \
                parent2.bits[cross_point1:cross_point2] + \
                parent1.bits[cross_point2:]
            child2.bits = parent2[:cross_point1] + \
                parent1.bits[cross_point1:cross_point2] + \
                parent2.bits[cross_point2:]

        return [child1, child2]

class TriplePointCrossing (BaseCrossing):
    def __init__(self, cross_probability):
        super().__init__(cross_probability)

    def cross(self, parent1: Chromosome, parent2: Chromosome) -> ChromosomeList:
        child1, child2 = parent1.copy(), parent2.copy()
        if rand() < self.cross_probability:
            cross_point1 = randint(1, parent1.chromosome_length)
            cross_point2 = randint(cross_point1, parent1.chromosome_length)
            cross_point3 = randint(cross_point2, parent1.chromosome_length)
            child1.bits = parent1[:cross_point1] + \
                parent2.bits[cross_point1:cross_point2] + \
                parent1.bits[cross_point2:cross_point3] + \
                parent2.bits[cross_point3:]
            child2.bits = parent2[:cross_point1] + \
                parent1.bits[cross_point1:cross_point2] + \
                parent2.bits[cross_point2:cross_point3] + \
                parent1.bits[cross_point3:]

        return [child1, child2]

class UniformCrossing (BaseCrossing):
    def __init__(self, cross_probability):
        super().__init__(cross_probability)

    def cross(self, parent1: Chromosome, parent2: Chromosome) -> ChromosomeList:
        child1, child2 = parent1.copy(), parent2.copy()
        if rand() < self.cross_probability:
            for i in range(parent1.chromosome_length, 2):
                    child1.bits[i], child2.bits[i] = child2.bits[i], child1.bits[i]

        return [child1, child2]


def crossing_enum(string):
    if string == "One point":
        return SinglePointCrossing
    if string == "Two point":
        return DoublePointCrossing
    if string == "Three point":
        return TriplePointCrossing
    if string == "Homogeneous":
        return SinglePointCrossing
