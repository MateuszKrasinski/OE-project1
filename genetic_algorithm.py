from population import Population


class GeneticAlgorithm:
    def __init__(self, objective_fun, bounds, chromosome_length, population_number, epoch, selectionStategy, crossStrategy, mutationStrategy):
        self.epochs_amount = epoch
        self.selection = selectionStategy
        self.cross = crossStrategy
        self.mutation = mutationStrategy
        self.objective = objective_fun
        self.population = Population(
            bounds, chromosome_length, population_number)

    def run(self):

        best, best_eval = 0, self.population.population[0].score(
            self.objective)

        for _ in range(self.epochs_amount):
            selected = self.selection.select(self.population, self.objective)
            scores = self.population.scoreAll(self.objective)
            for i in range(self.population.size):
                if scores[i] < best_eval:
                    best, best_eval = self.population.population[i], scores[i]

            next_epoch = self.population.create_next()
            for i in range(0, self.population.size, 2):
                # get selected parents in pairs
                parent1, parent2 = selected[i], selected[i+1]
                # crossover and mutation
                for c in self.cross.cross(parent1, parent2):
                    self.mutation.mutate(c)
                    next_epoch.population.append(c)
            self.population = next_epoch
        return [best, best_eval]
