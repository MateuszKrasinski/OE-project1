import tkinter as tk
import tkinter.ttk as ttk


class Gui:
    def __init__(self):
        self.result = None
        self.window = tk.Tk()
        self.initializeForm()

    def initializeForm(self):
        lbl_a1 = tk.Label(self.window, text="a1")
        lbl_a1.pack()
        a1 = tk.Entry(self.window)
        a1.pack()

        lbl_b1 = tk.Label(self.window, text="b1")
        lbl_b1.pack()
        b1 = tk.Entry(self.window)
        b1.pack()

        lbl_a2 = tk.Label(self.window, text="a2")
        lbl_a2.pack()
        a2 = tk.Entry(self.window)
        a2.pack()

        lbl_b2 = tk.Label(self.window, text="b2")
        lbl_b2.pack()
        b2 = tk.Entry(self.window)
        b2.pack()

        lbl_epochs = tk.Label(self.window, text="Epochs amount")
        lbl_epochs.pack()
        epochs = tk.Entry(self.window)
        epochs.pack()

        lbl_population = tk.Label(self.window, text="Population amount")
        lbl_population.pack()
        population = tk.Entry(self.window)
        population.pack()

        lbl_bits = tk.Label(self.window, text="Chromosome precision")
        lbl_bits.pack()
        bits = tk.Entry(self.window)
        bits.pack()

        lbl_mut_prob = tk.Label(self.window, text="Cross probability")
        lbl_mut_prob.pack()
        cross_prob = tk.Entry(self.window)
        cross_prob.pack()

        lbl_mut_prob = tk.Label(self.window, text="Mutation probability")
        lbl_mut_prob.pack()
        mut_prob = tk.Entry(self.window)
        mut_prob.pack()

        lbl_mut_prob = tk.Label(self.window, text="Selection probability")
        lbl_mut_prob.pack()
        sel_prob = tk.Entry(self.window)
        sel_prob.pack()

        lbl_alpha = tk.Label(self.window, text="Alpha")
        lbl_alpha.pack()
        alpha = tk.Entry(self.window)
        alpha.pack()

        lbl_beta = tk.Label(self.window, text="Beta")
        lbl_beta.pack()
        beta = tk.Entry(self.window)
        beta.pack()

        lbl_elitist = tk.Label(self.window, text="Elite strategy amount")
        lbl_elitist.pack()
        elite_amount = tk.Entry(self.window)
        elite_amount.pack()

        lbl_selection = tk.Label(self.window, text="Selection method")
        lbl_selection.pack()
        selection_method = ("Best", "Tournament", "Roulette")
        sel = ttk.Combobox(self.window, values=selection_method)
        sel.pack()

        lbl_crossover = tk.Label(self.window, text="Crossover method")
        lbl_crossover.pack()
        cross_method = ("Arithmetic", "Linear", "Average", "Blend Alpha", "Blend Alpha Beta")
        cross = ttk.Combobox(self.window, values=cross_method)
        cross.pack()

        lbl_mutation = tk.Label(self.window, text="Mutation method")
        lbl_mutation.pack()
        mutation_method = ("Uniform", "Gaussian")
        mut = ttk.Combobox(self.window, values=mutation_method)
        mut.pack()

        submit_button = tk.Button(self.window, text='Submit', command=lambda: self.submit(
            [[float(a1.get()), float(b1.get())], [float(a2.get()), float(b2.get())]],
            epochs.get(),
            population.get(),
            bits.get(),
            cross_prob.get(),
            mut_prob.get(),
            sel_prob.get(),
            elite_amount.get(),
            sel.get(),
            cross.get(),
            mut.get(),
            alpha.get(),
            beta.get()
        ))
        submit_button.pack()
        self.window.title('Generic algorithm')
        self.window.geometry("250x850+10+10")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def submit(self, bounds, epochs, pop, bits, cross_prob, mut_prob, sel_prob,
               elite_amount, cross, selection, mutation, alpha, beta):
        self.result = bounds, epochs, pop, bits, cross_prob, mut_prob, sel_prob, \
                      elite_amount, cross, selection, mutation, alpha, beta
        self.window.quit()

    def pop(self, time):
        self.popup_window(time)
        self.window.mainloop()

    def popup_window(self, time):
        window = tk.Toplevel()
        label = tk.Label(window, text="Czas wykonania programu:" + str(time) + "s")
        label.pack(fill='x', padx=50, pady=5)
        button_close = tk.Button(window, text="Close", command=window.destroy)
        button_close.pack(fill='x')

    def on_closing(self):
        self.result = None
        self.window.destroy()

if __name__ == '__main__':
    initializeForm()