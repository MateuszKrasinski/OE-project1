from numpy.random import rand


class Mutation:
    def __init__(self, mutation_probability):
        self.mutation_probability = mutation_probability

    def mutate(self, chromosome):
        for i in range(chromosome.chromosome_length):
            if rand() < self.mutation_probability:
                chromosome.bits[i] = 1 - chromosome.bits[i]
