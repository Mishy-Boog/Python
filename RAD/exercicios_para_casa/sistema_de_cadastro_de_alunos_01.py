class Aluno:

  def __init__(self: object, nome: str, idade: int, notas: float) -> None:
    self.nome = nome
    self.idade = idade
    self.notas = notas
  
  def calcular_media(self: object) -> float:
    return sum(self.notas) / len(self.notas) #divide a soma das notas pela quantidade das notas 

if __name__ == "__main__": #ver se ta no arquivo principal
  
  aluno1 = Aluno("Fulano", 40, [9.8, 7.6, 3.2])
  aluno2 = Aluno("Ciclano", 20, [8.1, 9.6, 7.2])
  lista_alunos = [aluno1, aluno2]

  for aluno in lista_alunos:
    print (f"Nome: {aluno.nome}, Idade: {aluno.idade}, Média: {aluno.calcular_media():.2f}")
