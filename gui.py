import tkinter as tk
import tkinter.ttk as ttk
import chromosome
import crossing_algorithms
import genetic_algorithm
import mutation_algorithms
import population

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

    lbl_cross_prob = tk.Label(window, text="Mutation probability %")
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
        cross_prob.get(),
        tournament_chrom.get(),
        sel.get(),
        cross.get(),
        mut.get(),
        best_proc.get(),
        elitist_proc.get(),
        inversion.get(),
    ))
    submit_button.pack()

    window.title('Generic algorithm')
    window.geometry("250x550+10+10")
    window.mainloop()


def submit(epochs, population, bits, tournament_chromosome, mut_prob, selection, cross,
           mutation, best_proc, function, elitist_proc, inversion):
    # TODO: submiting values


if __name__ == '__main__':
    initializeForm()