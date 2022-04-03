from numpy.random import rand, randint
from abc import ABC, abstractmethod

from chromosome import Chromosome


class BaseMutation(ABC):
    def __init__(self, mutation_probability):
        self.mutation_probability = mutation_probability

    @abstractmethod
    def mutate(self, chromosome: Chromosome) -> Chromosome:
        pass


class AllGenesMutation(BaseMutation):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def mutate(self, chromosome: Chromosome) -> Chromosome:
        for i in range(chromosome):
            if rand() < self.mutation_probability:
                chromosome[i] = 1 - chromosome[i]


class SingleGeneMutation(BaseMutation):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def mutate(self, chromosome: Chromosome) -> None:
        if rand() < self.mutation_probability:
            idx = randint(0, len(chromosome))
            chromosome[idx] = 1 - chromosome[idx]


class InversionMutation(BaseMutation):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def mutate(self, chromosome: Chromosome) -> None:
        if rand() < self.mutation_probability:
            idx1 = randint(0, randint(1, len(chromosome)))
            idx2 = randint(idx1, len(chromosome))
            chromosome[idx1:idx2] = chromosome[idx1:idx2][::-1]


class BoundaryMutation(BaseMutation):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def mutate(self, chromosome: Chromosome) -> None:
        if rand() < self.mutation_probability:
            helpRand = randint(-1, 1)
            if helpRand < 0:
                chromosome[0] = 1 - chromosome[0]
            else:
                chromosome[-1] = 1 - chromosome[-1]


class DoubleMutation(BaseMutation):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def mutate(self, chromosome: Chromosome) -> None:
        if rand() < self.mutation_probability:
            idx1 = randint(0, len(chromosome))
            idx2 = randint(0, len(chromosome))
            chromosome[idx1] = 1 - chromosome[idx1]
            chromosome[idx2] = 1 - chromosome[idx2]


def mutation_enum(string):
    if string == "One point":
        return SingleGeneMutation
    if string == "Two point":
        return DoubleMutation
    if string == "Boundary":
        return BoundaryMutation
    if string == "All":
        return AllGenesMutation