from numpy.random import randint
from numpy.random import rand


class Selection:
    # def __init__(self):
    # self.selected = []
    # self.selection_chance = selection_chance

    def selectAlgo(self, pop, scores, k=3):
        selection_ix = randint(pop.size)
        for ix in randint(0, pop.size, k-1):
            # check if better (e.g. perform a tournament)
            if scores[ix] < scores[selection_ix]:
                selection_ix = ix
        return pop.population[selection_ix]

    def select(self, pop, func):
        scores = pop.scoreAll(func)
        return [self.selectAlgo(pop, scores) for _ in range(pop.size)]
