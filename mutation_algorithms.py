from numpy.random import rand
from abc import ABC, abstractmethod

from chromosome import Chromosome

class BaseMutation (ABC):
    def __init__(self, mutation_probability):
        self.mutation_probability = mutation_probability

    @abstractmethod
    def mutate(self, chromosome: Chromosome) -> Chromosome:
        pass

class AllGenesMutation (BaseMutation):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def mutate(self, chromosome: Chromosome) -> Chromosome:
        for i in range(chromosome):
            if rand() < self.mutation_probability:
                chromosome[i] = 1 - chromosome[i]
