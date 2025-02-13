def verifica(a):
    if a > 0:
        print('numero positivo')
    elif a == 0:
        print('numero neutro')
    else:
        print('numero negativo')

def main():
    a = int(input('Digita um numero ae meno:'))
    verifica(a)

if __name__ == "__main__":
    main()


        

