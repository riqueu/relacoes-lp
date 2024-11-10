"""Módulo com a classe Instrumento e suas classes filhas Guitarra, Baixo e Violão"""

class Instrumento:
    def __init__(self, marca: str, modelo: str, preco: float, num_cordas: int) -> None:
        """Inicializa classe pai Instrumento.

        Args:
            marca (str): nome da marca
            modelo (str): modelo do instrumento
            preco (float): preço do instrumento
            num_cordas (int): número de cordas do instrumento
        """
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.num_cordas = num_cordas

class Guitarra(Instrumento):
    def __init__(self, marca: str, modelo: str, preco: float, num_cordas: int, tipo_captador: str) -> None:
        """Inicializa classe filha Guitarra.

        Args:
            marca (str): marca da guitarra
            modelo (str): modelo da guitarra
            preco (float): preço da guitarra
            num_cordas (int): número de cordas da guitarra
            tipo_captador (str): tipo de captador da guitarra
        """
        super().__init__(marca, modelo, preco, num_cordas)
        self.tipo_captador = tipo_captador

class Baixo(Instrumento):
    def __init__(self, marca: str, modelo: str, preco: float, num_cordas: int, tipo_madeira: str) -> None:
        """Inicializa classe filha Baixo.

        Args:
            marca (str): marca do baixo
            modelo (str): modelo do baixo
            preco (float): preço do baixo
            num_cordas (int): número de cordas do baixo
            tipo_madeira (str): tipo de madeira do baixo
        """
        super().__init__(marca, modelo, preco, num_cordas)
        self.tipo_madeira = tipo_madeira

class Violao(Instrumento):
    def __init__(self, marca: str, modelo: str, preco: float, num_cordas: int, tipo_corpo: str) -> None:
        """Inicializa classe filha Violão.

        Args:
            marca (str): marca do violão
            modelo (str): modelo do violão
            preco (float): preço do violão
            num_cordas (int): número de cordas do violão
            tipo_corpo (str): tipo de corpo do violão
        """
        super().__init__(marca, modelo, preco, num_cordas)
        self.tipo_corpo = tipo_corpo
