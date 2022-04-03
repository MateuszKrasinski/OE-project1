import tkinter as tk
import tkinter.ttk as ttk
import chromosome
import crossing_algorithms
import genetic_algorithm
import mutation_algorithms
import population
import selection_algorithms
import config

def initializeForm():
    window = tk.Tk()

    lbl_epochs = tk.Label(window, text="Epochs amount")
    lbl_epochs.pack()
    epochs = tk.Entry(window)
    epochs.pack()

    lbl_population = tk.Label(window, text="Population amount")
    lbl_population.pack()
    population = tk.Entry(window)
    population.pack()

    lbl_bits = tk.Label(window, text="Number of bits")
    lbl_bits.pack()
    bits = tk.Entry(window)
    bits.pack()

    lbl_begin = tk.Label(window, text="Begin")
    lbl_begin.pack()
    begin = tk.Entry(window)
    begin.pack()

    lbl_end = tk.Label(window, text="End")
    lbl_end.pack()
    end = tk.Entry(window)
    end.pack()

    lbl_cross_prob = tk.Label(window, text="Mutation probability %")
    lbl_cross_prob.pack()
    mutation_prob = tk.Entry(window)
    mutation_prob.pack()

    lbl_cross_prob = tk.Label(window, text="Cross probability %")
    lbl_cross_prob.pack()
    cross_prob = tk.Entry(window)
    cross_prob.pack()

    lbl_best_proc = tk.Label(window, text="Best selection procent %")
    lbl_best_proc.pack()
    best_proc = tk.Entry(window)
    best_proc.pack()

    lbl_elitist = tk.Label(window, text="Elitist strategy  %")
    lbl_elitist.pack()
    elitist_proc = tk.Entry(window)
    elitist_proc.pack()

    lbl_tournament_chrom = tk.Label(window, text="Tournament chromosome amount")
    lbl_tournament_chrom.pack()
    tournament_chrom = tk.Entry(window)
    tournament_chrom.pack()

    lbl_selection = tk.Label(window, text="Selection method")
    lbl_selection.pack()
    selection_method = ("Best", "Tournament", "Roulette")
    sel = ttk.Combobox(window, values=selection_method)
    sel.pack()

    lbl_crossover = tk.Label(window, text="Crossover method")
    lbl_crossover.pack()
    cross_method = ("One point", "Two point", "Three point", "Homogeneous")
    cross = ttk.Combobox(window, values=cross_method)
    cross.pack()

    lbl_mutation = tk.Label(window, text="Mutation method")
    lbl_mutation.pack()
    mutation_method = ("One point", "Two point", "Boundary")
    mut = ttk.Combobox(window, values=mutation_method)
    mut.pack()

    inversion = tk.IntVar()
    inv = tk.Checkbutton(window, text="Inversion", variable=inversion)
    inv.pack()

    submit_button = tk.Button(window, text='Submit', command=lambda: submit(
        epochs.get(),
        population.get(),
        bits.get(),
        begin.get(),
        end.get(),
        cross_prob.get(),
        mutation_prob.get(),
        sel.get(),
        cross.get(),
        mut.get(),
        elitist_proc.get(),
        inversion.get()
    )
                              )
    submit_button.pack()

    window.title('Generic algorithm')
    window.geometry("250x620+10+10")
    window.mainloop()


def submit(epochs, population, bits, begin, end, cross_prob,  mutation_prob, selection, cross,
           mutation, elitist_proc, inversion):
    gen = genetic_algorithm.GeneticAlgorithm(objective_fun=config.OBJECTIVE,
                                             bounds=[[begin, end]],
                                             chromosome_length= int(bits),
                                             population_number=int(population),
                                             epoch=int(epochs),
                                             selectionStategy=chooseSelectionMethods(selection),
                                             crossStrategy=chooseCrossMethods(cross),
                                             mutationStrategy=chooseMutationMethods(mutation),
                                             )
    gen.run()

def chooseSelectionMethods(method):
    return {
        "Best": selection_algorithms.BestSelection.select(),
        "Tournament": selection_algorithms.TournamentSelection.tournament,
        "Roulette": selection_algorithms.RouletteSelection.roulette
    }[method]

def chooseCrossMethods(method):
    return {
        "One point": crossing_algorithms.SinglePointCrossing.cross,
        "Two point": crossing_algorithms.DoublePointCrossing.cross,
        "Three point": crossing_algorithms.TriplePointCrossing.cross,
        #"Homogeneous":
    }[method]

def chooseMutationMethods(method):
    return {
        "One point": mutation_algorithms.SingleGeneMutation.mutate,
        "Two point": mutation_algorithms.doubleMutation.mutate,
        "Boundary": mutation_algorithms.boundaryMutation.mutate,
        "Inversion": mutation_algorithms.inversionMutation.mutate
    }[method]

def showResult(mean, timer):
    window = tk.Tk()

    lbl = tk.Label(window, text="Mean | Standard deviation")
    lbl.pack()
    mean_label = tk.Label(window, text=mean)
    mean_label.pack()

    lbl = tk.Label(window, text="Execution time")
    lbl.pack()
    time_label = tk.Label(window, text=timer)
    time_label.pack()

    quit_button = tk.Button(window, text='Close', command=window.destroy)
    quit_button.pack()

    window.title('Results')
    window.geometry("250x200+10+10")
    window.mainloop()

if __name__ == '__main__':
    initializeForm()