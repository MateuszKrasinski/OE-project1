from pyclbr import Function
from numpy.random import randint
import config
from chromosome import Chromosome

from population import Population

class EliteStrategy ():

    def __init__(self, elite_strategy_amount):
        self.elite_strategy_amount: int = elite_strategy_amount
        self.elite_chromosomes: list[Chromosome] = []


    def get_elites(self, population: Population) -> None:
        population.population.sort(key=lambda x: x.score(config.OBJECTIVE))
        pop_without_elites = population.create_next()
        pop_without_elites = population.population[self.elite_strategy_amount:]
        self.elite_chromosomes = population.population[:self.elite_strategy_amount]
        population.population = pop_without_elites

    def add_elites(self, pop: Population) -> None:
         pop.population = pop.population + self.elite_chromosomes