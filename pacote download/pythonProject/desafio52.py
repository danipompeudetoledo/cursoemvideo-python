# n= int(input('Digite um número: '))
# contador=0
# for c in range(0,n+1):
#  print('{}'.format(c),end=' ')
#
#  if n%c ==0:
#      print('não')
#      contador=contador+1
#
#
# else:
#     print('sim')
#     contador = contador + 1
# print('o numero {} foi divisivel {} vezes '.format(n,contador))





# solução do guanabara
num= int(input('Digite um numero:'))
tot=0
for c in range(1,num+1):
     if num % c == 0:
         print('\33[33m')
         tot=tot+1
     else:
         print('\033[31m')
     print('{}'.format(c),end=' ')
print('\n\033 O numero {} foi divisivel {} vezes'.format(num,tot))
if tot==2:
    print('E por isso ele é  primo')
else:
    print('E por isso ele não é primo')

