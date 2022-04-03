import random

import numpy as np

from crossing_algorithms import BaseCrossing
from mutation_algorithms import BaseMutation
from population import Population
from selection_algorithms import BaseSelection
from elite_algorithm import EliteStrategy
from inversion import InversionMutation
import matplotlib.pyplot as plt


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
        self.avg = 0
        self.best_evals = []
        self.standard_deviations = []
        self.standard_deviation = 0
        self.avgs = []
        self.file = open('results/genetic_file.txt', 'w')
        self.file_avg = open('results/avg.txt', 'w')
        self.file_standard_deviation = open('results/standard_deviation.txt', 'w')

    def evaluation(self):
        self.scores = self.population.scoreAll(self.objective)
        sum_ = 0
        for i in range(len(self.population.population)):
            if self.scores[i] < self.best_eval:
                self.best, self.best_eval = self.population[i], self.scores[i]
            sum_ += self.scores[i]
        self.avg = sum_ / len(self.population.population)
        self.standard_deviation = np.std(self.scores)
        self.best_evals.append(self.best_eval)
        self.avgs.append(self.avg)
        self.standard_deviations.append(self.standard_deviation)

    def draw_plot_best(self):
        plt.figure()
        plt.xlabel("epochs")
        plt.ylabel("best fitness")
        plt.plot([i for i in range(len(self.best_evals))], self.best_evals)
        plt.savefig('results/best_fitness.png')

    def draw_plot_avg(self):
        plt.figure()
        plt.xlabel("epochs")
        plt.ylabel("avg")
        plt.plot([i for i in range(len(self.avgs))], self.avgs)
        plt.savefig('results/avgs.png')

    def draw_plot_sd(self):
        plt.figure()
        plt.xlabel("epochs")
        plt.ylabel("standard deviation")
        plt.plot([i for i in range(len(self.standard_deviations))], self.standard_deviations)
        plt.savefig('results/sd.png')

    def selection(self):
        self.population = self.selection_stategy.select(self.population, self.objective)

    def remove_elites_from_population(self):
        self.elite_strategy.get_elites(self.population)

    def add_elites_to_population(self):
        self.elite_strategy.add_elites(self.population)

    def cross_and_mutate(self) -> Population:
        # next_epoch = self.population.create_next()
        # for i in range(0, self.population, 2):
        #     # get selected parents in pairs
        #     parent1, parent2 = self.population[i], self.population[i + 1]
        #     # crossover and mutation
        #     for c in self.crossing_strategy.cross(parent1, parent2):
        #         self.mutation_strategy.mutate(c)
        #         self.inversion_strategy.inversion(c)
        #         next_epoch.append(c)
        # return next_epoch

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
            # print(len(self.population.population))
            self.population = self.cross_and_mutate()
            # print(len(self.population.population))
            self.add_elites_to_population()
            print(epoch_number, self.best_eval, self.avg, self.standard_deviation, len(self.population.population))
            self.file.write("%s %s\n" % (epoch_number, self.best_eval))
            self.file_avg.write("%s %s\n" % (epoch_number, self.avg))
            self.file_standard_deviation.write("%s %s\n" % (epoch_number, self.standard_deviation))
        self.draw_plot_best()
        self.draw_plot_avg()
        self.draw_plot_sd()
