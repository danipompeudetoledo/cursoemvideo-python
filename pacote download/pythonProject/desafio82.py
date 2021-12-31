lista=list()
pares=list()
impares=list()
while True:
    n=int(input('Digite um número: '))
    lista.append(n)

    if n%2==0:
     pares.append(n)
    elif n%2==1:
        impares.append(n)

    op= str(input('Quer continuar? S/N '))
    if op in 'Nn':
        break

print(f'A lista completa é {lista} ')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')