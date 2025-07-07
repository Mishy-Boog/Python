from dataclasses import dataclass
@dataclass 

class Produto:
  nome: str
  preco: float
  quantidade: int

produto1 = Produto("Caneta", 1.90, 10)


print(produto1.nome, produto1.preco, produto1.quantidade)
