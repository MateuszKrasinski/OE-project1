from abc import ABC
from enum import Enum
from pyclbr import Function
from numpy.random import randint
from abc import ABC, abstractmethod
import numpy as np
import config
from chromosome import Chromosome

from population import Population


class BaseSelection(ABC):
    def __init__(self, selection_probability):
        self.selection_probability = selection_probability
    @abstractmethod
    def select(self, pop: Population, func: Function) -> Population:
        pass


class TournamentSelection(BaseSelection):

    def tournament(self, population: Population, scores: list[float], k=3) -> Chromosome:
        selection_ix = randint(population)
        for ix in randint(0, population, k - 1):
            if scores[ix] < scores[selection_ix]:
                selection_ix = ix
        return population[selection_ix]

    def select(self, pop: Population, func: Function) -> Population:
        scores = pop.scoreAll(func)
        selection = pop.create_next()
        selection.population = [self.tournament(pop, scores) for _ in range(int(len(pop.population) * self.selection_probability ))]
        return selection


class BestSelection(BaseSelection):

    def select(self, pop: Population, func: Function) -> Population:
        selection_ix = pop.size
        scores = pop.scoreAll(config.OBJECTIVE)
        pop.population.sort(key=lambda x: x.score(config.OBJECTIVE))
        scores2 = pop.scoreAll(config.OBJECTIVE)
        selection = pop.create_next()

        selection.population = pop.population[:int(selection_ix*0.2)]
        scores3 = selection.scoreAll(config.OBJECTIVE)
        return selection


# TODO COPOILT DID IT CHECK IT PLEASE
class RouletteSelection(BaseSelection):

    # def select(self, pop: Population, func: Function) -> Population:
    #     scores = pop.scoreAll(func)
    #     selection = pop.create_next()
    #     selection.population = [pop.population[i] for i in self.roulette(scores)]
    #     return selection
    #
    # def roulette(self, scores: list[float]) -> list[int]:
    #     roulette = [0]
    #     for i in range(1, len(scores)):
    #         roulette.append(roulette[i-1] + scores[i-1])
    #     return [i for i in range(len(scores)) if roulette[i] > randint(roulette[-1])]

    def calculateDistribution(self, population):
        min_func_val = min([ind.score(config.OBJECTIVE) for ind in population])
        scale = abs(min_func_val) + 1 if min_func_val < 0 else 0

        values = [1 / (ind.score(config.OBJECTIVE) + scale) for ind in population]
        sum_func = sum(1 / v for v in values)

        probabilities = [val / sum_func for val in values]
        distributions = [probabilities[0]]

        for i in range(1, len(probabilities)):
            distributions.append(distributions[i - 1] + probabilities[i])
        return distributions

    def select(self, population, func: Function) -> Population:
        distributions = self.calculateDistribution(population)
        values = tuple(zip(population, distributions))
        random_prob = np.random.uniform(min(distributions), max(distributions))
        result = values[0][0]
        for ind, d in values:
            if d < random_prob:
                result = ind
            else:
                break
        return result

class Selection(Enum):
    Best = BestSelection
    Tournament = TournamentSelection
    Roulette = RouletteSelection

