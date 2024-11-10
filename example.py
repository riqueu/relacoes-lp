"""Módulo de exemplo"""

from loja_instrumentos.loja import Loja
from loja_instrumentos.funcionario import Funcionario
from loja_instrumentos.instrumento import Guitarra, Baixo, Violao

# Criando lojas
loja1 = Loja("São Paulo")
loja2 = Loja("Rio de Janeiro")
loja3 = Loja("Maceió")

# Setando lojas mais próximas
loja1.definir_loja_mais_proxima(loja2)
loja2.definir_loja_mais_proxima(loja1)
loja3.definir_loja_mais_proxima(loja2)

# Criando funcionários
funcio1 = Funcionario("David Byrne", "12345678910", 3000.00, "Vendedor")
funcio2 = Funcionario("Geordie Greep", "09876543210", 3500.00, "Gerente")
funcio3 = Funcionario("Phil Elverum", "12312312300", 3000.00, "Vendedor")

# Adicionando funcionários às lojas
loja1.adicionar_funcionario(funcio1)
loja1.adicionar_funcionario(funcio2)
loja1.adicionar_funcionario(funcio3)

# Criando instrumentos
guitarra = Guitarra("Gibson", "Les Paul", 2499.99, 6, "Humbuckers")
baixo = Baixo("Ibanez", "SR300", 1799.95, 4, "Maple")
violao = Violao("Yamaha", "F310", 1099.90, 6, "Dreadnought")

# Adicionando instrumentos ao estoque
loja1.adicionar_instrumento(guitarra)
loja1.adicionar_instrumento(baixo)
loja1.adicionar_instrumento(violao)

# Consultando estoque
print("Consultando estoque:")
print(f"Loja 1: {loja1.consultar_estoque()}")
print(f"Loja 2: {loja2.consultar_estoque()}")
print(f"Loja 3: {loja3.consultar_estoque()}")

# Funcionários pré-remanejamento
print("Funcionários pré-remanejamento:")
print(f"Loja 1: {loja1.consultar_funcionarios()}")
print(f"Loja 2: {loja2.consultar_funcionarios()}")
print(f"Loja 3: {loja3.consultar_funcionarios()}")

# Remanejando funcionário
funcio2.mudar_loja(loja2)
funcio3.mudar_loja(loja3)

# Funcionários pós-remanejamento
print("Funcionários pós-remanejamento:")
print(f"Loja 1: {loja1.consultar_funcionarios()}")
print(f"Loja 2: {loja2.consultar_funcionarios()}")
print(f"Loja 3: {loja3.consultar_funcionarios()}")
