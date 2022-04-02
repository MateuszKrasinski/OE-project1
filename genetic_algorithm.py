from chromosome import Chromosome
from crossing_algorithms import BaseCrossing
from mutation_algorithms import BaseMutation
from population import Population
from selection_algorithms import BaseSelection
from elite_algorithm import EliteStrategy
from inversion import InversionMutation


class GeneticAlgorithm:
    def __init__(self, objective_fun, bounds: list[list[float]],
                 chromosome_length: int, population_number: int, epoch: int,
                 selectionStategy: BaseSelection, crossStrategy: BaseCrossing, mutationStrategy: BaseMutation,
                 elite_strategy: EliteStrategy, inversion_strategy: InversionMutation):
        self.epochs_amount = epoch
        self.selection_stategy = selectionStategy
        self.crossing_strategy = crossStrategy
        self.mutation_strategy = mutationStrategy
        self.elite_strategy = elite_strategy
        self.inversion_strategy = inversion_strategy
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

    def remove_elites_from_population(self):
        self.elite_strategy.get_elites(self.population)

    def add_elites_to_population(self):
        self.elite_strategy.add_elites(self.population)

    def cross_and_mutate(self) -> Population:
        next_epoch = self.population.create_next()
        for i in range(0, self.population, 2):
            # get selected parents in pairs
            parent1, parent2 = self.population[i], self.population[i + 1]
            # crossover and mutation
            for c in self.crossing_strategy.cross(parent1, parent2):
                self.mutation_strategy.mutate(c)
                self.inversion_strategy.inversion(c)
                next_epoch.append(c)
        return next_epoch

    def run(self) -> list[int, float]:
        for epoch_number in range(self.epochs_amount):
            self.remove_elites_from_population()
            self.evaluation()
            self.selection()
            self.population = self.cross_and_mutate()
            self.add_elites_to_population()
            print(epoch_number, self.best_eval)
        # return [self.best, self.best_eval]
