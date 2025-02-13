# Inicializa uma lista vazia
notas = []

# Laço para ler 4 notas
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota (entre 0 e 10): "))
    
    # Verifica se a nota está entre 0 e 10
    while nota < 0 or nota > 10:
        print("Nota inválida! A nota deve ser entre 0 e 10.")
        nota = float(input(f"Digite a {i+1}ª nota (entre 0 e 10): "))
    
    notas.append(nota)

# Exibe as notas
print("\nAs notas digitadas são:", notas)

# Calcula a média das notas
media = sum(notas) / len(notas)

# Exibe a média
print(f"A média das notas é: {media:.2f}")
