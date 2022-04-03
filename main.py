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
            bounds, epochs, pop, bits, cross_prob, mut_prob, sel_prob, inversion_prob, tournament_chromosomes,\
                elite_amount, selection_str, cross_str, mutation_str = gui.result
            cross = crossing_enum(cross_str)(float(cross_prob))
            mutation = mutation_enum(mutation_str)(float(mut_prob))
            elite_strategy = EliteStrategy(int(elite_amount))
            inversion_strategy = InversionMutation(float(inversion_prob))
            selection = Selection[selection_str].value(float(sel_prob))
            algorithm = GeneticAlgorithm(config.OBJECTIVE, bounds, int(bits),
                                         int(pop), int(epochs), selection, cross, mutation,
                                         elite_strategy, inversion_strategy)
            algorithm.run()
            end = time.time()
            time_elapsed = end - start
            gui.pop(time_elapsed)
            if gui.result is None:
                exit()
