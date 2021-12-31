# print('Gerador de PA')
# print('-=' * 10)
# primeiro=int(input('Primeiro termo: '))
# razao=int(input('Razão da PA: '))
# termo=primeiro
# cont=1
# total=0
# mais=10
# while mais!=0:
#    total+=mais
#    while cont<= total:
#       print('{} ->' .format(termo), end=' ')
#       termo+=razao
#       cont += 1
#    print('PAUSA')
#    mais = int(input('\n Quantos termos vc que mostrar a mais?'))
# print('Progressão finalizada com {} termos mostrados'.format(total))


















print('Gerador de PA')
print('-='*10)
termo=int(input('Digite o primeiro termo'))
razao= int(input('Digite a razão'))
cont=1
total=0
mais=10
while mais != 0:
   total+=mais
   while cont<= total:
         print('{} ->'.format(termo),end=' ')
         termo += razao
         cont+=1
   print('pausa')
   mais=int(input('Quantos termos que digitar a mais'))
print("Progressão finalizada com {} termos mostrados".format(total))
