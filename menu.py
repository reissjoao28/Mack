def menu():
    print('1 - Soma dos dois números digitados')
    print('2 - Diferença dos dois números digitados')
    print('3 - Produto dos dois números digitados')
    print('4 - Divisão dos dois números digitados')
    print('0 - Sair')

    while True:
        opcao = int(input("Qual a sua opcao?"))
        if opcao in [0,1,2,3,4]:
            return opcao
        else:
            print ("opcao invalida")

def soma(n1,n2):
    return  n1 + n2

def subtracao(n1,n2):
    return n1 - n2

def vezes(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

def main():
    n1 = int(input("Qual o primeiro numero"))
    n2 = int(input("Qual o segundo numero"))

    while True:
        opcao = menu()

        if opcao == 1:
            print(f"Resultado da soma: {soma(n1, n2)}")
        elif opcao == 2:
            print(f"Resultado da diferença: {subtracao(n1, n2)}")
        elif opcao == 3:
            print(f"Resultado do produto: {vezes(n1, n2)}")
        elif opcao == 4:
            print(f"Resultado da divisão: {divisao(n1, n2)}")
        elif opcao == 0:
            print("Saindo do programa. Até mais!")
            break

if __name__ == "__main__":
    main()
