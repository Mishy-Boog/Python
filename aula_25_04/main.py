from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

pessoa1 = Pessoa(cpf=12345678900, nome="Maria", nascimento=date(1984,7,26), oculos=False)

marca1 = Marca(id=1, nome="FIAT UNO", sigla="FIA")

veiculo1 = Veiculo(placa="Lua1l97", cor="Roxo", proprietario= pessoa1, marca=marca1)

pessoa2 = Pessoa(cpf=123123131123, nome= "Paulo", nascimento=date(1907, 2, 9),oculos=True)

marca2 = Marca(id=2, nome="Monza", sigla="MNZ")

veiculo2 = Veiculo(placa="lpj2n98", cor="Bege", proprietario= pessoa2, marca=marca2)

print(veiculo2)
print(veiculo1)