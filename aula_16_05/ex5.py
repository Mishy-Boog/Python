import tkinter as tk

janela = tk.Tk()
fome = tk.Label(
        #fg = foreground, bg= background
    text= "a",
    foreground="red",
    background ="black",
    width=40,
    height=40
)

entry = tk.Entry()

entry.insert(0,"sahdjkjhdagsj")
entry.get()
entry.pack()
fome.pack()



janela.mainloop()