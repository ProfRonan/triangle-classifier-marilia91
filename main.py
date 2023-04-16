
while True: 
    a = int(input("digite um número inteiro: "))
    b = int(input("digite um número inteiro: "))
    c = int(input("digite um número inteiro: "))
    break

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print ('Equilátero')
    elif a == b or a == c or b == c:
        print('Isósceles')
    else:
         print('Escaleno')
else: 
    print('Não é um triângulo')
    
