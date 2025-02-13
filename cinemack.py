def inicializar_dados():
    filmes = [
        {"nome": "Filme 1", "preco": 20.0, "capacidade": [50, 50], "poltronas": [[0] * 50, [0] * 50]},
        {"nome": "Filme 2", "preco": 15.0, "capacidade": [40, 40], "poltronas": [[0] * 40, [0] * 40]},
        {"nome": "Filme 3", "preco": 10.0, "capacidade": [30, 30], "poltronas": [[0] * 30, [0] * 30]}
    ]
    return filmes

def exibir_menu():
    print("\nMenu Principal:")
    print(" 1. Comprar ingressos")
    print(" 2. Avaliar um filme")
    print(" 3. Encerrar o dia e exibir o relatório")

def escolher_poltrona(poltronas_disponiveis, capacidade):
    while True:
        try:
            print("\nMapa de poltronas (0 = Livre, 1 = Ocupada):")
            print(" ".join(map(str, poltronas_disponiveis)))
            poltrona = int(input(f"Escolha uma poltrona (0 a {capacidade - 1}): "))
            if 0 <= poltrona < capacidade and poltronas_disponiveis[poltrona] == 0:
                poltronas_disponiveis[poltrona] = 1
                print(f"Poltrona {poltrona} reservada com sucesso!")
                return
            else:
                print("Poltrona inválida ou já ocupada. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def comprar_ingresso(filmes):
    print("\nFilmes disponíveis:")
    for i, filme in enumerate(filmes):
        print(f"{i + 1}. {filme['nome']} (R$ {filme['preco']:.2f})")

    try:
        filme_escolhido = int(input("\nEscolha um filme (1 a 3): ")) - 1
        if filme_escolhido < 0 or filme_escolhido >= len(filmes):
            print("Opção inválida.")
            return

        sessao = int(input("Escolha a sessão (1 ou 2): ")) - 1
        if sessao not in [0, 1]:
            print("Sessão inválida.")
            return

        capacidade_disponivel = filmes[filme_escolhido]["capacidade"][sessao]
        if capacidade_disponivel == 0:
            print("Sessão lotada!")
            return

        qtd = int(input("Quantos ingressos deseja comprar? "))
        if qtd <= 0 or qtd > capacidade_disponivel:
            print("Quantidade inválida!")
            return

        for _ in range(qtd):
            escolher_poltrona(filmes[filme_escolhido]["poltronas"][sessao], len(filmes[filme_escolhido]["poltronas"][sessao]))

        filmes[filme_escolhido]["capacidade"][sessao] -= qtd
        print(f"{qtd} ingressos comprados com sucesso para o {filmes[filme_escolhido]['nome']} - Sessão {sessao + 1}.")

    except ValueError:
        print("Entrada inválida. Tente novamente.")

def avaliar_filme(filmes, avaliacoes):
    print("\nEscolha um filme para avaliar:")
    for i, filme in enumerate(filmes):
        print(f"{i + 1}. {filme['nome']}")

    try:
        filme_escolhido = int(input()) - 1
        if filme_escolhido < 0 or filme_escolhido >= len(filmes):
            print("Opção inválida.")
            return

        nota = int(input("Dê uma nota de 1 a 5: "))
        if nota < 1 or nota > 5:
            print("Nota inválida.")
            return

        avaliacoes[filmes[filme_escolhido]['nome']].append(nota)
        print(f"Obrigado por avaliar o {filmes[filme_escolhido]['nome']}!")

    except ValueError:
        print("Entrada inválida. Tente novamente.")

def exibir_relatorio(filmes, avaliacoes):
    print("\nRelatório Final:")
    for filme in filmes:
        print(f"\n{filme['nome']}:")
        total_ingressos = sum(sum(sessao) for sessao in filme['poltronas'])
        print(f"  Total de ingressos vendidos: {total_ingressos}")
        media_avaliacao = sum(avaliacoes[filme['nome']]) / len(avaliacoes[filme['nome']]) if avaliacoes[filme['nome']] else 0
        print(f"  Média de avaliação: {media_avaliacao:.1f} estrelas")

def main():
    filmes = inicializar_dados()
    avaliacoes = {filme['nome']: [] for filme in filmes}

    while True:
        exibir_menu()
        try:
            opcao = int(input("\nEscolha uma opção: "))
            if opcao == 1:
                comprar_ingresso(filmes)
            elif opcao == 2:
                avaliar_filme(filmes, avaliacoes)
            elif opcao == 3:
                exibir_relatorio(filmes, avaliacoes)
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

if __name__ == "__main__":
    main()