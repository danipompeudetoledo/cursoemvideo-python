# print('Gerador de PA')
# print('-=' * 10)
# primeiro=int(input('Primeiro termo: '))
# razao=int(input('Razão da PA: '))
# decimo= primeiro+(10-1)*razao
# for c in range(primeiro,decimo+razao,razao):
#     print('{}'.format(c),end=' ')


print('Gerador de PA')
print('-=' * 10)
primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))
termo=primeiro
c=1

while c<=10:
   print('{} ->' .format(termo),end=' ')
   termo+=razao
   c += 1
print('FIM')
