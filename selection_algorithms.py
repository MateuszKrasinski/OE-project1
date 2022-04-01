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