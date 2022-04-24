import time
import config
from selection_algorithms import Selection
from crossing_algorithms import crossing_enum
from genetic_algorithm import GeneticAlgorithm
from elite_algorithm import EliteStrategy
from mutation_algorithms import mutation_enum
from gui import Gui

if __name__ == '__main__':
    gui = Gui()
    while True:
        if gui.result is not None:
            start = time.time()
            bounds, epochs, pop, bits, cross_prob, mut_prob, sel_prob, \
            elite_amount, selection_str, cross_str, mutation_str, alpha, beta = gui.result
            if cross_str == "Blend Alpha":
                cross = crossing_enum(cross_str)(float(cross_prob), float(alpha))
            elif cross_str == "Blend Alpha Beta":
                cross = crossing_enum(cross_str)(float(cross_prob), float(alpha), float(beta))
            else:
                cross = crossing_enum(cross_str)(float(cross_prob))
            mutation = mutation_enum(mutation_str)(float(mut_prob))
            elite_strategy = EliteStrategy(int(elite_amount))
            selection = Selection[selection_str].value(float(sel_prob))
            algorithm = GeneticAlgorithm(config.OBJECTIVE, bounds, int(bits),
                                         int(pop), int(epochs), selection, cross, mutation,
                                         elite_strategy, alpha, beta)
            algorithm.run()
            end = time.time()
            time_elapsed = end - start
            gui.pop(time_elapsed)
            if gui.result is None:
                exit()
