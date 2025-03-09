class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas  # Lista de notas
    
    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas) #sum soma os valores e len conta quantos elementos tem
        return 0  # Retorna 0 se não houver notas

# Cria uma lista para armazenar alunos
alunos = [
    Aluno("Jean", 20, [7.5, 8.0, 9.0]),
    Aluno("Maria", 22, [6.5, 7.0, 8.5]),
    Aluno("Whindersson", 19, [5.0, 6.5, 7.5])
]

# Exibe a média das notas de cada aluno
for aluno in alunos:
    print(f"Aluno: {aluno.nome}, Média: {aluno.calcular_media():.2f}")

