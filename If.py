n1 = str(input("Qual o primeiro nome:"))
n2 = str(input("Qual o segundo nome:"))

if n1.lower() < n2.lower():
    print(n1, n2) 
else:
    print(n2, n1)