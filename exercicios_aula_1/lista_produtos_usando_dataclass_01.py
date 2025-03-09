from dataclasses import dataclass
@dataclass 

class Produto:
  nome: str
  preco: float
  quantidade: int

lista_produtos = [
  ("manga", 1.90, 10),
  ("uva", 1.90, 40),
  ("pera", 1.90, 20),
]

print(lista_produtos)
