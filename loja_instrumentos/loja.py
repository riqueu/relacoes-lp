"""Módulo com a classe Loja"""

from loja_instrumentos.funcionario import Funcionario
from loja_instrumentos.instrumento import Instrumento, Guitarra, Baixo, Violao

class Loja:
    def __init__(self, localizacao: str) -> None:
        """Inicializa uma loja.

        Args:
            localizacao (str): Localização da loja.
        """
        self.localizacao = localizacao
        self.funcionarios = []
        self.estoque = []
        self.loja_mais_proxima = None

    def adicionar_funcionario(self, funcionario: Funcionario) -> None:
        """Função que adiciona um funcionário à loja.

        Args:
            funcionario (Funcionario): objeto da classe Funcionario a ser adicionado.
        """
        self.funcionarios.append(funcionario)
        funcionario.loja_atual = self

    def remover_funcionario(self, funcionario: Funcionario) -> None:
        """Função que remove um funcionário à loja.

        Args:
            funcionario (Funcionario): objeto da classe Funcionario a ser removido.
        """
        self.funcionarios.remove(funcionario)
        funcionario.loja_atual = None

    def adicionar_instrumento(self, instrumento: Instrumento) -> None:
        """Função que adiciona um instrumento ao estoque da loja.

        Args:
            instrumento (Instrumento): objeto da classe Instrumento a ser adicionado.
        """
        self.estoque.append(instrumento)

    def remover_instrumento(self, instrumento: Instrumento) -> None:
        """Função que remove um instrumento do estoque da loja.

        Args:
            instrumento (Instrumento): objeto da classe Instrumento a ser removido.
        """
        self.estoque.remove(instrumento)

    def consultar_estoque(self) -> dict:
        """Função que retorna a quantidade de instrumentos de cada tipo no estoque.

        Returns:
            dict: Dicionário com a quantidade de instrumentos de cada tipo no estoque.
        """
        contagem = {"Guitarra": 0, "Baixo": 0, "Violao": 0}
        for instrumento in self.estoque:
            if isinstance(instrumento, Guitarra):
                contagem["Guitarra"] += 1
            elif isinstance(instrumento, Baixo):
                contagem["Baixo"] += 1
            elif isinstance(instrumento, Violao):
                contagem["Violao"] += 1
        return contagem

    def consultar_funcionarios(self) -> dict:
        """Função que retorna a quantidade de funcionários de cada cargo na loja.

        Returns:
            dict: Dicionário com a quantidade de funcionários de cada cargo na loja.
        """
        contagem = {}
        for funcionario in self.funcionarios:
            if funcionario.cargo in contagem:
                contagem[funcionario.cargo] += 1
            else:
                contagem[funcionario.cargo] = 1
        return contagem

    def definir_loja_mais_proxima(self, loja: 'Loja') -> None:
        """Função que define a loja mais próxima.

        Args:
            loja (Loja): objeto da classe Loja que é a loja mais próxima.
        """
        self.loja_mais_proxima = loja
