from dataclasses import dataclass
from aula_25_04.pessoa import Pessoa
from aula_25_04.marca import Marca

@dataclass
class Veiculo:
    placa: str
    cor: str
    proprietario: Pessoa
    marca: Marca