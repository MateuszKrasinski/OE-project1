import config
from selection_algorithms import TournamentSelection
from crossing_algorithms import SinglePointCrossing
from genetic_algorithm import GeneticAlgorithm
from mutation_algorithms import AllGenesMutation

if __name__ == '__main__':
    selection = TournamentSelection()
    cross = SinglePointCrossing(config.CROSS_PROBABILITY)
    mutation = AllGenesMutation(config.MUTATION_PROBABILITY)

    algorithm = GeneticAlgorithm(config.OBJECTIVE, config.BOUNDS, config.CHROMOSOME_LENGTH,
                            config.POPULATION_AMOUNT, config.NUMBER_OF_EPOCHS, selection, cross, mutation)
    best, score = algorithm.run()
    print(best.decode())
    print(score)
