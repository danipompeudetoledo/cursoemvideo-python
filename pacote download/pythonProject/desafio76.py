print('-'*40)
print('{:^40}'.format(' LISTAGEM DE PREÇOS '))
print('-'*40)

# produtos= ('Lápis','.'*30 ,'R$','1.75',
#            '\nBorracha','.'*30,'R$','2.00',
#            '\nCaderno','.'*30,'R$','15.90',
#            '\nEstojo','.'*30,'R$','25.00',
#            "\nTransferidor",'.'*30,'4.20',
#            "\nCompasso",'.'*30,'R$','9.99',
#            "\nMochila",'.'*30,'R$','120.32',
#            "\nCanetas",'.'*30,'R$','22.30',
#            "\nLivro",'.'*30,'R$','34.90')
# for p in produtos:
#     print(p,end=' ')

produtos = ('Lápis','1.75',
                'Borracha', '2.00',
                'Caderno', '15.90',
                'Estojo', '25.00',
                "Transferidor", '4.20',
                "Compasso",'9.99',
                "Mochila",'120.32',
                "Canetas",'22.30',
                "Livro",  '34.90')
for p in range(0,len(produtos)):
    if p %2==0:
        print(f'{produtos[p]:.<30}',end=' ')
    else:
        print(f'R${produtos[p]:>8}')

print('-'*40)














