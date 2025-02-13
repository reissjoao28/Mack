def exibeMsg():
    print('Este programa é um conversor de unidades entre C e F:')

def verificaOpcao():
    letra = input(str('Digite F ou C:'))
    if letra == "C":
        return letra
    elif letra == 'F':
        return letra
    else:
        print("letra invalida")

def verificaIntervalo():
    inicio = float(input('digite o valor inicial do intervalo:'))
    fim = float(input("digite um valor final para o intervalo:"))
    if inicio > fim:
        print('o valor final deve ser maior')
    else:
        return inicio, fim


def exibeFtoC(inicio, fim):
    print('convertendo de Fahrenheit para Celsius')
    for fahrenheit in range(int(inicio), int(fim) + 1):
        celsius = (fahrenheit - 32)/ 1.8
        print(f'{fahrenheit}ºF = {celsius}ºC')

def exibeCtoF(inicio, fim):
    print('convertendo de c para f')
    for celsius in range(int(inicio), int(fim) + 1):
        fahrenheit = (celsius * 1.8)+ 32
        print(f'{celsius}ºC = {fahrenheit}ºF')

def main():
    exibeMsg()
    letra = verificaOpcao()
    inicio, fim = verificaIntervalo()

    if letra == "F":
        return exibeFtoC(inicio,fim)
    elif letra == "C":
        return exibeCtoF(inicio,fim)

if __name__ == "__main__":
    main()