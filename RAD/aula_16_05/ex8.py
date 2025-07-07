import tkinter as tk

def ao_focar(event):
    if entrada.get() == "Digite seu nome aqui!":
        entrada.delete(0, "end")
        entrada.config(fg="black") #altera a cor do texto

def ao_desfocar(event):
    if not entrada.get():
        entrada.insert(0, "Digite o seu nome aqui!")
        entrada.config(fg="gray") #altera a cor do texto


janela = tk.Tk()
entrada = tk.Entry(width=40, bg="white", fg="gray")
entrada.pack()
entrada.insert(0, "Digite seu nome aqui!")

#Quando a caixa dde entrada ganha o foco, chame a função ao_focar
entrada.bind("<FocusIn>", ao_focar)

#Quando a caixa dde entrada ganha o foco, chame a função ao_desfocar
entrada.bind("<FocusOut>", ao_desfocar)

janela.mainloop()
