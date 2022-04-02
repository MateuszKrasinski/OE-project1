import config
from selection_algorithms import TournamentSelection, BestSelection, RouletteSelection
from crossing_algorithms import SinglePointCrossing, DoublePointCrossing, TriplePointCrossing
from genetic_algorithm import GeneticAlgorithm
from elite_algorithm import EliteStrategy
from mutation_algorithms import AllGenesMutation, SingleGeneMutation, DoubleMutation, BoundaryMutation
from inversion import InversionMutation

if __name__ == '__main__':
    selection = TournamentSelection()
    cross = TriplePointCrossing(config.CROSS_PROBABILITY)
    mutation = AllGenesMutation(config.MUTATION_PROBABILITY)
    elite_strategy = EliteStrategy(config.ELITE_AMOUNT)
    inversion_strategy = InversionMutation(config.INVERSION_PROBABILITY)

    algorithm = GeneticAlgorithm(config.OBJECTIVE, config.BOUNDS, config.CHROMOSOME_LENGTH,
                            config.POPULATION_AMOUNT, config.NUMBER_OF_EPOCHS, selection, cross, mutation,
                                 elite_strategy, inversion_strategy)
    algorithm.run()
