cont=0
lista=list()
while True:
    valor= int( input("Digite um valor: "))

    if valor not in lista:
        lista.append(valor)
        lista.sort(reverse=True)

    op=str(input("Quer continuar? [S/N] "))
    cont+=1
    if op in 'Nn':
        break



print('-='*20)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente foram {lista}')
if 5 in lista:
        print('O valor 5 faz parte da lista')
else:
        print('O valor 5 não foi encontrado na  lista')