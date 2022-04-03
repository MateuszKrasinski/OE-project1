from numpy.random import rand, randint
from chromosome import Chromosome


class InversionMutation():
    def __init__(self, inversion_probability):
        self.inversion_probability = inversion_probability

    def inversion(self, chromosome: Chromosome) -> None:
        if rand() < self.inversion_probability:
            idx1 = randint(0, randint(1, len(chromosome)))
            idx2 = randint(idx1, len(chromosome))
            chromosome[idx1:idx2] = chromosome[idx1:idx2][::-1]
