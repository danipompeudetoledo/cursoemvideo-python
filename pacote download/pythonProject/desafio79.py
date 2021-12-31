# valor=[]
#
# while True:
#   n=int(input(f'Digite uma valor: '))
#   if n not in valor:
#    valor.append(n)
#    print('Valor adicionado com sucesso!')
#   else:
#
#
#
#     print('numero repetido.Não vou adicionar')
#
#
#
#
#   op = str(input('Quer continuar [s/n]')).strip().upper()
#
#   if op in 'nN':
#      break
#
# print(f'Você digitou os valores {sorted(valor)}')
#
#







valor=list()
while True:
 n=int(input('Digite um valor: '))
 if n not in valor:
     valor.append(n)
     print('Valor adicionado com sucesso')

 else:
     print('Valor repetido')

 op=str(input('Quer continuar? [S/N] '))
 if op in'nN':
    break
print(f'Você digitou os valores {sorted(valor)}')















