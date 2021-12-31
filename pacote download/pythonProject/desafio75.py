# num1=(int(input("Digite um número:")),int(input("Digite outro número:")),int(input("Digite mais um numero:")),
#                 int(input("DIGITE O ULTIMO NUMERO")))

# cont=0
#
# num=(int(input("Digite um número:")),
#     int(input("Digite outro número:")),
#     int(input("Digite mais um numero:")),
#     int(input("DIGITE O ULTIMO NUMERO")))
# print('Você digitou os valores {}'.format(num))
# print('O valor 9 apareceu {} vezes'.format(num.count(9)))
# if 3 in num:
#  print('o valor 3 apareceu  na posição {}ª'.format(num.index(3)+1))
#  print('o valor 3 não foi digitado em nenhuma posição')
# print('os numeros pares foram ',end=' ')
# for n in num:
#  if n%2==0:
#   print(n,end=' ')
  # print('os numeros pares foram {}'.format(pares))



# num_alunos = 4
# nomes = []
# notas = []
# media = 0
# for i in range(num_alunos):
#     nomes.append(input('Informe o nome do aluno: '))
#     notas.append(float(input('Informe a nota de ' + nomes[i] + ': ')))
#     media = media + notas[i]
#     media = media / num_alunos
# print('A media da turma eh ', media)
# for i in range(num_alunos):
#  if notas[i] > media:
#   print('Parabens', nomes[i])


# n = int(input('Digite um numero: '))
# lista = []
# for i in range(2,n+1,2):
#  lista = lista + [i]
#  print(lista)

num=(int(input('digite um numero: ')),
     int(input("Digite outro ")),
     int(input("Digite outro ")),
     int(input ("Digite o ultimo ")))
print('Você digitou os valores {}'.format(num))
if num.count(9) > 1:
 print(('o valor 9 apareceu {} vezes'.format(num.count(9))))
else:
    print("o valor 9 apareceu {} vez".format(num.count(9)))
if 3 in num:
 print("O valor 3 apareceu  na {}ª posição ".format(num.index(3)+1))
else:
     print("O valor 3 não foi digitado")
print("Os valores pares  digitados foram: ",end=' ')
for n in num:
     if n%2==0:
          print(n,end=', ')














