from abc import ABC
from pyclbr import Function
from numpy.random import randint
from abc import ABC, abstractmethod

import config
from chromosome import Chromosome

from population import Population


class BaseSelection (ABC):
    @abstractmethod
    def select(self, pop: Population, func: Function) -> Population:
        pass


class TournamentSelection:

    def tournament(self, population: Population, scores: list[float], k=3) -> Chromosome:
        selection_ix = randint(population)
        for ix in randint(0, population, k-1):
            if scores[ix] < scores[selection_ix]:
                selection_ix = ix
        return population[selection_ix]

    def select(self, pop: Population, func: Function) -> Population:
        scores = pop.scoreAll(func)
        selection = pop.create_next()
        selection.population = [self.tournament(pop, scores) for _ in range(pop)]
        return selection

class BestSelection:

    def select(self, pop: Population, func: Function) -> Population:
        selection_ix = pop.size
        pop.population.sort(key=lambda x: x.score(config.OBJECTIVE))
        selection = pop.create_next()
        selection.population = pop.population[:selection_ix]
        return selection

# TODO COPOILT DID IT CHECK IT PLEASE
class RouletteSelection:

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
        min_func_val = min(population.decodeAll())
        scale = abs(min_func_val) + 1 if min_func_val < 0 else 0
        values = [1 / (ind.decode() + scale) for ind in population]
        sum_func = sum(1 / v for v in values)
        # prawdopodobienstwa dla kazdego osobnika
        probabilities = [val / sum_func for val in values]
        distributions = [probabilities[0]]

        for i in range(1, len(probabilities)):
            distributions.append(distributions[i - 1] + probabilities[i])
        return distributions

    def rouletteSelection(self, population):
        distributions = self.calculateDistributions(self, population)
        values = tuple(zip(population, distributions))
        random_prob = np.random.uniform(min(distributions), max(distributions))
        result = values[0][0]
        for ind, d in values:
            if d < random_prob:
                result = ind
            else:
                break
        return result
