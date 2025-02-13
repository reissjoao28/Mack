def entrada():
    numero = int(input('digite um numero'))
    if numero < 0:
        print('numero invalido')
    else:
        return numero
    

def calculaSoma(a,b,c):
    soma = a+b+c
    return soma

def main():
    numeros = []
    for i in range(3):
        numero = entrada()
        numeros.append(numero)

    soma = calculaSoma(*numeros)

    print(f"A soma dos números {numeros[0]}, {numeros[1]} e {numeros[2]} é: {soma}")

if __name__ == "__main__":
    main()