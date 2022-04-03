import time
import config
from selection_algorithms import TournamentSelection, BestSelection, RouletteSelection, Selection
from crossing_algorithms import SinglePointCrossing, DoublePointCrossing, TriplePointCrossing, crossing_enum
from genetic_algorithm import GeneticAlgorithm
from elite_algorithm import EliteStrategy
from mutation_algorithms import AllGenesMutation, SingleGeneMutation, DoubleMutation, BoundaryMutation, mutation_enum
from inversion import InversionMutation
from gui import Gui


if __name__ == '__main__':
    gui = Gui()
    while True:
        if gui.result is not None:
            start = time.time()
            epochs, pop, bits, mut_prob, inversion, tournament_chromosomes, elite_amount, selection_str, cross_str, mutation_str = gui.result
            cross = crossing_enum(cross_str)(config.CROSS_PROBABILITY)
            mutation = mutation_enum(mutation_str)(config.MUTATION_PROBABILITY)
            elite_strategy = EliteStrategy(config.ELITE_AMOUNT)
            inversion_strategy = InversionMutation(config.INVERSION_PROBABILITY)
            selection = Selection[selection_str].value(config.SELECTION_PROBABILITY)
            algorithm = GeneticAlgorithm(config.OBJECTIVE, config.BOUNDS, config.CHROMOSOME_LENGTH,
                                         config.POPULATION_AMOUNT, config.NUMBER_OF_EPOCHS, selection, cross, mutation,
                                         elite_strategy, inversion_strategy)
            algorithm.run()
            end = time.time()
            time_elapsed = end - start
            gui.pop(time_elapsed)
            if gui.result is None:
                exit()
