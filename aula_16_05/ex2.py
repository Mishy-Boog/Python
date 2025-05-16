import tkinter as tk

janela = tk.Tk()
fome = tk.Label(
        #fg = foreground, bg= background
    text="Python é rad",
    foreground="red",
    background ="black",
    width=40,
    height=40
)

fome.pack()


janela.mainloop()