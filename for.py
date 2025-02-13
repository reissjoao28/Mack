# Leitura da quantidade de empregados
quantidade = int(input("Digite a quantidade de empregados: "))

# Inicializando variáveis para cálculos
total_reajustado = 0
quantidade_10_reajuste = 0  # Contador para empregados com reajuste de 10%

# Laço para processar cada empregado
for i in range(quantidade):
    nome = input("Digite o nome do funcionário: ")
    salario = float(input(f"Digite salário do {nome}: "))
    
    # Calculando o reajuste conforme a tabela
    if salario >= 3000:
        reajuste = 0.08
    elif salario >= 2000:
        reajuste = 0.10
        quantidade_10_reajuste += 1
    else:
        reajuste = 0.12
    
    novo_salario = salario * (1 + reajuste)
    
    # Exibe o salário reajustado
    print(f"O novo salário de {nome} é {novo_salario:.2f}")
    
    # Acumulando para cálculo do salário médio
    total_reajustado += novo_salario

# Calculando o salário médio
salario_medio = total_reajustado / quantidade

# Exibindo a quantidade de empregados com reajuste de 10%
print(f"\nQuantidade de funcionários que receberam 10% de aumento: {quantidade_10_reajuste}")

# Exibindo o salário médio após o reajuste
print(f"Salário médio dos funcionários (após reajuste): {salario_medio:.2f}")
