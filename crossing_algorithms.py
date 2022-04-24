import random
from abc import ABC, abstractmethod
from numpy.random import rand

import config
from chromosome import Chromosome, ChromosomeList


class BaseCrossing(ABC):
    def __init__(self, cross_propability):
        self.cross_probability = cross_propability
        super().__init__()

    @abstractmethod
    def cross(self, parent1: Chromosome, parent2: Chromosome) -> ChromosomeList:
        pass

class AverageCross(BaseCrossing):
    def __init__(self, cross_probability):
        super().__init__(cross_probability)

    def cross(self, parent1: Chromosome, parent2: Chromosome) -> ChromosomeList:
        child1 = parent1.copy()
        if rand() < self.cross_probability:
            x1 = parent1.first_gene
            y1 = parent1.second_gene
            x2 = parent2.first_gene
            y2 = parent2.second_gene
            x1_new = (x1 + x2) / 2
            y1_new = (y1 + y2) / 2
            child1.set_first_gene(x1_new)
            child1.set_second_gene(y1_new)

            if child1.areGenesInBounds():
                return [child1]
        return [parent1]


class ArithmeticCross(BaseCrossing):
    def __init__(self, cross_probability):
        super().__init__(cross_probability)

    def cross(self, parent1: Chromosome, parent2: Chromosome) -> ChromosomeList:
        child1, child2 = parent1.copy(), parent2.copy()
        if rand() < self.cross_probability:
            x1 = parent1.first_gene
            y1 = parent1.second_gene
            x2 = parent2.first_gene
            y2 = parent2.second_gene
            k = random.uniform(0, 1)
            child1.set_first_gene(k * x1 + (1 - k) * x2)
            child1.set_second_gene(k * y1 + (1 - k) * y2)
            child2.set_first_gene((1 - k) * x1 + k * x2)
            child2.set_second_gene((1 - k) * y1 + k * y2)
            if child1.areGenesInBounds() and child2.areGenesInBounds():
                return [child1, child2]
        return [parent1, parent2]


class LinearCross(BaseCrossing):
    def __init__(self, cross_probability):
        super().__init__(cross_probability)

    def cross(self, parent1: Chromosome, parent2: Chromosome) -> ChromosomeList:
        child1, child2, child3 = parent1.copy(), parent2.copy(), parent2.copy()
        children = []
        if rand() < self.cross_probability:
            x1 = parent1.first_gene
            y1 = parent1.second_gene
            x2 = parent2.first_gene
            y2 = parent2.second_gene
            k = random.uniform(0, 1)
            child1.set_first_gene(1 / 2 * x1 + 1 / 2 * x2)
            child1.set_second_gene(1 / 2 * y1 + 1 / 2 * y2)
            children.append(child1)
            child2.set_first_gene(3 / 2 * x1 - 1 / 2 * x2)
            child2.set_second_gene(3 / 2 * y1 - 1 / 2 * y2)
            children.append(child2)
            child3.set_first_gene(-1 / 2 * x1 + 3 / 2 * x2)
            child3.set_second_gene(-1 / 2 * y1 + 3 / 2 * y2)
            children.append(child3)
            children.sort(key=lambda x: x.score(config.OBJECTIVE))
            if children[0].areGenesInBounds() and children[1].areGenesInBounds():
                return children[:2]
        return [parent1, parent2]


class BlendCrossAlpha(BaseCrossing):
    def __init__(self, cross_probability, alpha):
        super().__init__(cross_probability)
        self.alpha = alpha

    def cross(self, parent1: Chromosome, parent2: Chromosome) -> ChromosomeList:
        child1, child2, child3 = parent1.copy(), parent2.copy(), parent2.copy()
        children = []
        if rand() < self.cross_probability:
            x1 = parent1.first_gene
            y1 = parent1.second_gene
            x2 = parent2.first_gene
            y2 = parent2.second_gene
            d1 = abs(x1 - x2)
            d2 = abs(y1 - y2)
            x1_new = random.uniform((min(x1, x2) - self.alpha * d1), (max(x1, x2) - self.alpha * d1))
            y1_new = random.uniform((min(y1, y2) - self.alpha * d1), (max(y1, y2) - self.alpha * d2))
            x2_new = random.uniform((min(x1, x2) - self.alpha * d1), (max(x1, x2) - self.alpha * d1))
            y2_new = random.uniform((min(y1, y2) - self.alpha * d1), (max(y1, y2) - self.alpha * d2))
            child1.set_first_gene(x1_new)
            child1.set_second_gene(y1_new)
            child2.set_first_gene(x2_new)
            child2.set_second_gene(y2_new)
            if child1.areGenesInBounds() and child2.areGenesInBounds():
                return [child1, child2]
        return [parent1, parent2]


class BlendCrossAlphaBeta(BaseCrossing):
    def __init__(self, cross_probability, alpha, beta):
        super().__init__(cross_probability)
        self.alpha = alpha
        self.beta = beta

    def cross(self, parent1: Chromosome, parent2: Chromosome) -> ChromosomeList:
        child1, child2 = parent1.copy(), parent2.copy()
        if rand() < self.cross_probability:
            x1 = parent1.first_gene
            y1 = parent1.second_gene
            x2 = parent2.first_gene
            y2 = parent2.second_gene
            d1 = abs(x1 - x2)
            d2 = abs(y1 - y2)
            x1_new = random.uniform((min(x1, x2) - self.alpha * d1), (max(x1, x2) - self.beta * d1))
            y1_new = random.uniform((min(y1, y2) - self.alpha * d1), (max(y1, y2) - self.beta * d2))
            x2_new = random.uniform((min(x1, x2) - self.alpha * d1), (max(x1, x2) - self.beta * d1))
            y2_new = random.uniform((min(y1, y2) - self.alpha * d1), (max(y1, y2) - self.beta * d2))
            child1.set_first_gene(x1_new)
            child1.set_second_gene(y1_new)
            child2.set_first_gene(x2_new)
            child2.set_second_gene(y2_new)
            if child1.areGenesInBounds() and child2.areGenesInBounds():
                return [child1, child2]
        return [parent1, parent2]


def crossing_enum(string):
    if string == "Blend Alpha Beta":
        return BlendCrossAlphaBeta
    if string == "Blend Alpha":
        return BlendCrossAlpha
    if string == "Linear":
        return LinearCross
    if string == "Arithmetic":
        return ArithmeticCross
    if string == "Average":
        return AverageCross
