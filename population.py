from __future__ import annotations

from chromosome import Chromosome


class Population:
    def __init__(self, bounds: list[list[float]], chromosome_accuracy: int, population_number: int, createPopul=True):
        self.size = population_number
        self.bounds = bounds
        self.chromosome_accuracy = chromosome_accuracy
        self.population = []
        if createPopul:
            self.population = [Chromosome(chromosome_accuracy, bounds)
                               for _ in range(population_number)]

    def scoreAll(self, desired_function: function) -> list[float]:
        return [desired_function([p.first_gene, p.second_gene]) for p in self.population]

    def create_next(self) -> Population:
        return Population(self.bounds, self.chromosome_accuracy, self.size, False)

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
