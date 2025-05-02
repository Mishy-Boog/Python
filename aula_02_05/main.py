from banco_de_dados import BancoDeDados
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

if __name__ == "__main__":

    banco = BancoDeDados()

    banco.conectar()

    banco.criar_tabelas()

    pessoa1 = Pessoa(cpf=12345678900, nome="Maria", nascimento="2000-01-01", oculos=True)
    banco.inserir_pessoa(pessoa1)

banco.fechar_conexao()
