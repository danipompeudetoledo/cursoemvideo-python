num1=int(input('Primeiro valor: '))
num2=int(input('Segundo valor: '))
from time import sleep
maior=num1

opcao=0
while opcao != 5:
  print('''  [1] Somar
  [2] Multiplicar
  [3] Maior
  [4] Novos Números
  [5] Sair do programa''')
  opcao= int(input('>>>>>>Qual é a sua opção? '))

  if opcao==1:
     soma=num1+num2
     print("A soma entre {} e {} é {} ".format(num1,num2,soma))

  elif opcao ==2:
     m=num1*num2
     print('A Multiplicação entre {} x {} é {}'.format(num1,num2,m))

  elif opcao==3:
     if num1> num2:
       maior=num1

     else:
       maior=num2
     print('Entre {} e {} o maior valor é {}'.format(num1,num2,maior))
  elif opcao==4:
      print('Informe os numeros novamente')
      num1 = int(input('Primeiro valor: '))
      num2 = int(input('Segundo valor: '))

      sleep(2)

  elif opcao== 5:
      print('Finalizando...')

  else:
    print('Opção invalida.Tente novamente')
  print('=-='*20)
print('Fim do programa. Volte sempre!')



# solução do guanabara
#  n1=int(input("Primeiro valor"))
#  n2=int(input("Segundo valor"))
#  opção=0
#  whil
#  print('''[1] Somar
#  [2] Multipilcar
#  [3] Maior
#  [4] Novos Numeros
#  [5] Sair do programa''')
#  opção =str(input('Qual é a sua opção? '))









