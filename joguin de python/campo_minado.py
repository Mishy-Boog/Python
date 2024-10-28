import tkinter as tk
import random
import pygame
import tkinter.messagebox
from PIL import Image, ImageTk

class CampoMinado:
    def __init__(self, master, size=8, bombs=10):
        self.master = master
        self.size = size
        self.bombs = bombs
        self.board = [[0] * size for _ in range(size)]
        self.buttons = [[None] * size for _ in range(size)]
        self.game_over = False

        self.place_bombs()
        self.create_buttons()

        # Iniciar o Pygame e tocar o áudio de fundo
        pygame.mixer.init()
        pygame.mixer.music.load("musicafreddy.wav")  # Exemplo de arquivo de áudio
        pygame.mixer.music.play(-1)  # -1 para tocar em loop

    def place_bombs(self):
        bomb_positions = random.sample(range(self.size * self.size), self.bombs)
        for pos in bomb_positions:
            x = pos // self.size
            y = pos % self.size
            self.board[x][y] = -1

            # Atualiza contagens de bombas adjacentes
            for i in range(max(0, x - 1), min(self.size, x + 2)):
                for j in range(max(0, y - 1), min(self.size, y + 2)):
                    if self.board[i][j] != -1:
                        self.board[i][j] += 1

    def create_buttons(self):
        for i in range(self.size):
            for j in range(self.size):
                # Define cores alternadas para o estilo de xadrez
                bg_color = "white" if (i + j) % 2 == 0 else "black"
                button = tk.Button(self.master, width=4, height=2, bg=bg_color,
                                   command=lambda x=i, y=j: self.reveal(x, y))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def reveal(self, x, y):
        if self.game_over:
            return

        if self.board[x][y] == -1:
            self.buttons[x][y].config(text="B", bg="red")
            self.game_over = True
            self.play_explosion_sound()  # Tocar o som da explosão
            self.show_game_over_image()  # Mostrar a imagem de fim de jogo
            self.end_game()
        else:
            self.buttons[x][y].config(text=str(self.board[x][y]), bg="lightgrey")
            self.buttons[x][y].config(state="disabled")
            if self.board[x][y] == 0:
                self.auto_reveal(x, y)

    def auto_reveal(self, x, y):
        for i in range(max(0, x - 1), min(self.size, x + 2)):
            for j in range(max(0, y - 1), min(self.size, y + 2)):
                if self.buttons[i][j]['state'] != 'disabled':
                    self.reveal(i, j)

    def play_explosion_sound(self):
        explosion_sound = pygame.mixer.Sound("jumpscare.wav")  # Caminho para o arquivo de áudio
        explosion_sound.play()

    def show_game_over_image(self):
        game_over_image = Image.open("jumpscarefreddy.jpeg")  # Altere para o seu arquivo JPEG
        game_over_image = game_over_image.resize((300, 200), Image.LANCZOS)  # Redimensionar se necessário
        self.game_over_photo = ImageTk.PhotoImage(game_over_image)

        # Criar um label para exibir a imagem
        label = tk.Label(self.master, image=self.game_over_photo)
        label.image = self.game_over_photo  # Manter uma referência
        label.grid(row=self.size, columnspan=self.size)  # Ajuste a posição conforme necessário

    def end_game(self):
        for i in range(self.size):
            for j in range(self.size):
                self.buttons[i][j].config(state="disabled")
        pygame.mixer.music.stop()  # Para a música ao fim do jogo
        tk.messagebox.showinfo("Fim de Jogo", "Você perdeu!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Campo Minado")
    game = CampoMinado(root)
    root.mainloop()
