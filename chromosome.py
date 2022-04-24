from __future__ import annotations

import random

from numpy.random import randint


class Chromosome:
    def __init__(self, chromosome_accuracy, bounds):
        self.bounds = bounds
        self.chromosome_accuracy = chromosome_accuracy
        self.first_gene = round(random.uniform(bounds[0][0], bounds[0][1]), chromosome_accuracy)
        self.second_gene = round(random.uniform(bounds[1][0], bounds[1][1]), chromosome_accuracy)

    def score(self, desired_function: function) -> float:
        return desired_function([self.first_gene, self.second_gene])

    def copy(self) -> Chromosome:
        copy = Chromosome(self.chromosome_accuracy, self.bounds)
        copy.first_gene = self.first_gene
        copy.second_gene = self.second_gene
        return copy

    def set_first_gene(self, first_gene):
        self.first_gene = round(first_gene, self.chromosome_accuracy)

    def set_second_gene(self, second_gene):
        self.second_gene = round(second_gene, self.chromosome_accuracy)

    def __str__(self) -> str:
        return [str(self.first_gene), (self.second_gene)].__str__()

    def areGenesInBounds(self):
        if self.bounds[0][0] <= self.first_gene <= self.bounds[0][1] and self.bounds[1][0] <= self.second_gene <= self.bounds[1][1]:
            return True
        return False
ChromosomeList = list[Chromosome]
