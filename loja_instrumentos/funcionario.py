"""Módulo com a classe Funcionario"""

class Funcionario:
    def __init__(self, nome: str, cpf: str, salario: float, cargo: str) -> None:
        """Inicializa um funcionário.

        Args:
            nome (str): nome do funcionário
            cpf (str): cpf do funcionário (string para manter os zeros à esquerda)
            salario (float): salário do funcionário
            cargo (str): cargo do funcionário
        """
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
        self.loja_atual = None

    def mudar_loja(self, nova_loja) -> None:
        """Função que muda o funcionário de loja.

        Args:
            nova_loja (Loja): objeto da classe Loja para onde o funcionário será transferido.
        """
        if self.loja_atual:
            self.loja_atual.remover_funcionario(self)
        nova_loja.adicionar_funcionario(self)
        self.loja_atual = nova_loja
