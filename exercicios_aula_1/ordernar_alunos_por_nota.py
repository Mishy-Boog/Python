alunos = [
  {"nome": "Fulano", "nota": 8.7},
  {"nome": "Ciclano", "nota": 7.6},
  {"nome": "Beltrano", "nota": 5.9},
]

alunos_ordernados = sorted(alunos, key=lambda aluno: aluno["nota"])
print(alunos_ordenados)
