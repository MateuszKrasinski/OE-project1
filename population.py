from __future__ import annotations

from chromosome import Chromosome


class Population:
    def __init__(self, bounds: list[list[float]], chromosome_length: int, population_number: int, createPopul=True):
        self.size = population_number
        self.bounds = bounds
        self.chromosome_length = chromosome_length
        self.population = []
        if createPopul:
            self.population = [Chromosome(chromosome_length, bounds)
                               for _ in range(population_number)]

    def decodeAll(self) -> list[float]:
        return [p.decode() for p in self.population]

    def scoreAll(self, desired_function: function) -> list[float]:
        return [desired_function(p.decode()) for p in self.population]

    def create_next(self) -> Population:
        return Population(self.bounds, self.chromosome_length, self.size, False)

    def append(self, list):
        self.population.append(list)

    def __index__(self):
        return len(self.population)

    def __getitem__(self, key):
        return self.population[key]

    def __setitem__(self, key, value):
        self.population[key] = value

    def __iter__(self):
        return iter(self.population)
