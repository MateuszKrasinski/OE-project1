from chromosome import Chromosome
from crossing_algorithms import BaseCrossing
from mutation_algorithms import BaseMutation
from population import Population
from selection_algorithms import BaseSelection


class GeneticAlgorithm:
    def __init__(self, objective_fun, bounds: list[list[float]],
                 chromosome_length: int, population_number: int, epoch: int,
                 selectionStategy: BaseSelection, crossStrategy: BaseCrossing, mutationStrategy: BaseMutation):
        self.epochs_amount = epoch
        self.selection_stategy = selectionStategy
        self.crossing_strategy = crossStrategy
        self.mutation_strategy = mutationStrategy
        self.objective = objective_fun
        self.population = Population(
            bounds, chromosome_length, population_number)
        self.scores = []
        self.best = 0
        self.best_eval = self.population[0].score(self.objective)

    def evaluation(self):
        self.scores = self.population.scoreAll(self.objective)
        for i in range(self.population):
            if self.scores[i] < self.best_eval:
                self.best, self.best_eval = self.population[i], self.scores[i]

    def selection(self):
        self.population = self.selection_stategy.select(self.population, self.objective)

    def cross_and_mutate(self) -> Population:
        next_epoch = self.population.create_next()
        for i in range(0, self.population, 2):
                # get selected parents in pairs
                parent1, parent2 = self.population[i], self.population[i+1]
                # crossover and mutation
                for c in self.crossing_strategy.cross(parent1, parent2):
                    self.mutation_strategy.mutate(c)
                    next_epoch.append(c)
        return next_epoch

    def run(self) -> list[Chromosome, float]:
        for _ in range(self.epochs_amount):
            self.evaluation()
            self.selection()
            self.population = self.cross_and_mutate()
        return [self.best, self.best_eval]
