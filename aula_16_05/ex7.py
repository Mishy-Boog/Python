import tkinter as tk

border_effects = {
    "reto": tk.FLAT,
    "afundado": tk.SUNKEN,
    "elevado": tk.RAISED,
    "borda": tk.GROOVE,
    "ondulado": tk.RIDGE,
}

janela = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master = janela, relief= relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master = frame, text= relief_name)
    label.pack()

janela.mainloop()