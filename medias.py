# Lista para armazenar as médias dos alunos
medias = []

# Laço para ler as notas de 10 alunos
for i in range(10):
    print(f"\nAluno {i+1}:")
    notas = []
    
    # Leitura das 4 notas do aluno
    for j in range(4):
        nota = float(input(f"Digite a {j+1}ª nota (entre 0 e 10): "))
        
        # Validação da nota
        while nota < 0 or nota > 10:
            print("Nota inválida! A nota deve ser entre 0 e 10.")
            nota = float(input(f"Digite a {j+1}ª nota (entre 0 e 10): "))
        
        notas.append(nota)
    
    # Calculando a média do aluno
    media = sum(notas) / len(notas)
    medias.append(media)

# Exibindo as médias dos alunos
print("\nMédias dos alunos:")
print(medias)

# Contando o número de alunos com média maior ou igual a 7.0
alunos_acima_7 = sum(1 for media in medias if media >= 7.0)

# Exibindo o número de alunos com média >= 7.0
print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_acima_7}")
