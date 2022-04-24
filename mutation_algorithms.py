import random

from numpy.random import rand
from abc import ABC, abstractmethod

from chromosome import Chromosome


class BaseMutation(ABC):
    def __init__(self, mutation_probability):
        self.mutation_probability = mutation_probability

    @abstractmethod
    def mutate(self, chromosome: Chromosome) -> Chromosome:
        pass


class UniformMutation(BaseMutation):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def mutate(self, chromosome: Chromosome) -> None:
        if rand() < self.mutation_probability:
            if random.randrange(0, 2) == 0:
                chromosome.first_gene = random.uniform(chromosome.bounds[0][0], chromosome.bounds[0][1])
            else:
                chromosome.second_gene = random.uniform(chromosome.bounds[1][0], chromosome.bounds[1][1])


class GaussianMutation(BaseMutation):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def mutate(self, chromosome: Chromosome) -> None:
        if rand() < self.mutation_probability:
            while True:
                adder = random.gauss(0, 1)
                if chromosome.bounds[0][0] <= chromosome.first_gene + adder <= chromosome.bounds[0][1]:
                    chromosome.first_gene = chromosome.first_gene + adder
                    break
            while True:
                adder = random.gauss(0, 1)
                if chromosome.bounds[0][0] <= chromosome.second_gene + adder <= chromosome.bounds[0][1]:
                    chromosome.second_gene = chromosome.second_gene + adder
                    break


def mutation_enum(string):
    if string == "Uniform":
        return UniformMutation
    if string == "Gaussian":
        return GaussianMutation
