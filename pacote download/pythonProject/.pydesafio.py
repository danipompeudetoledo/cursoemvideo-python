print('-'*20)
print('{:-^40}'.format('LOJAS SUPER BARATÃO'))
print('-'*20)
total=0
maiormil=0
mais_barato=0
cont=0
barato=''
while True:
    nome=str(input("Nome do produto ")).upper()
    preco=float(input('Preço R$ '))
    cont+=1
    if cont==1:
        mais_barato=preco
        barato=nome
    else:
        if preco < mais_barato:
            mais_barato=preco

    if preco> 1000:
        maiormil+=1
    total+=preco
    resp=" "
    while resp not in 'SN':
     resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
             break
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos um {nome} custando mais de 1000,00')
print(f'O produto mais barato foi {barato} e custa R$ {mais_barato:.2f}')
print('{:-^40}'.format('Fim do programa'))



