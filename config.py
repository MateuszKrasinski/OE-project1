import math

POPULATION_AMOUNT = 100
NUMBER_OF_EPOCHS = 500
CROSS_PROBABILITY = 0.8
MUTATION_PROBABILITY = 0.01
BOUNDS = [[-1.5, 4.0], [-3.0, 4.0]]
CHROMOSOME_LENGTH = 32

def OBJECTIVE(x: list[float]) -> float:
	return math.sin(x[0] + x[1]) + pow((x[0] - x[1]), 2) - 1.5 * x[0] + 2.5 * x[1] + 1