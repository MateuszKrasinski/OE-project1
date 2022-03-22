import math
from selection import Selection
from cross import Cross
from genetic_algorithm import GeneticAlgorithm
from mutation import Mutation

POPULATION_AMOUNT = 200
NUMBER_OF_EPOCHS = 1000
CROSS_PROBABILITY = 0.8
MUTATION_PROBABILITY = 0.01
BOUNDS = [[-1.5, 4.0], [-3.0, 4.0]]
CHROMOSOME_LENGTH = 32

def objective(x):
	return math.sin(x[0] + x[1]) + pow((x[0] - x[1]), 2) - 1.5 * x[0] + 2.5 * x[1] + 1

if __name__ == '__main__':

    selection = Selection()
    cross = Cross(CROSS_PROBABILITY)
    mutation = Mutation(MUTATION_PROBABILITY)

    algo = GeneticAlgorithm(objective, BOUNDS, CHROMOSOME_LENGTH, POPULATION_AMOUNT, NUMBER_OF_EPOCHS, selection, cross, mutation )
    best, score = algo.run()
    print(best)
    print(score)
