# from random import randint
# print("-="*20)
# print(('Vamos jogar  PAR OU IMPAR '))
# print(("-="*20))
# contador = 0
#
# while True :
#        valor = int(input("Diga um valor: "))
#        computador = randint(0, 11)
#        soma = computador + valor
#        pi= ' '
#        while pi not in "PI":
#          pi = str(input('Par ou impar? [P/I]')).strip().upper()[0]
#          print("Você jogou {} e o computador jogou {}. Total de {} ".format(valor, computador, soma))
#          print('Deu par' if soma % 2==0 else 'Deu impar'  )
#
#        if pi=='P':
#           if soma % 2==0 :
#            print("Você venceu")
#            contador += 1
#
#           else:
#            print('Você perdeu!')
#            break
#
#
#
#        elif pi=='I':
#            if soma % 2==1:
#                print('Você venceu')
#                contador += 1
#            else:
#              print("Você perdeu")
#              break
#
#        print("Vamos jogar novamente")
# print("GAME OVER! Voce venceu {} vezes".format(contador))

from random import randint
print("-="*20)
print(" Vamos jogar PAR OU IMPAR")
print("-="*20)
total=0
cont=0
while True:
    valor=int(input("digite um valor: "))
    computador= randint(0,11)
    total = computador+valor
    tipo=''
    while tipo not in 'PI':
      tipo=str(input("Par ou impar [P/I]")).strip().upper()[0]
      print("Você jogou {} e o computador {} . Total de {}".format(valor,computador,total ))
      print( "Deu pár"if total % 2==0 else "Deu impar")

    if tipo == 'P':
        if  total %2 == 0 :
              print("Você venceu")
              cont+=1

        else:
            print('Você perdeu')
            break

    elif tipo=='I':
                 if total%2==1:
                   print('Voce venceu')
                   cont+=1
                 else:
                   print('vOCÊ PERDEU')
                   break
print("Vamos jogar novamente")
print("Game over! Você venceu {} vezes".format(cont))

































