# from time import sleep
# from random import randint
# print('Sou seu computador...')
# sleep(2)
# print("Acabei de pensar em um numero entre 0 e 10 . ")
# print('Será que você consegue adivinhar qual foi? ')
# tentativas=0
# computador= randint(0,10)
# palpite=int(input('Qual é o seu palpite '))
# while palpite != computador:
#     if palpite < computador:
#         print("Mais...Tente mais uma vez")
#         palpite=(int(input("Qual é o seu palpite ")))
#         tentativas+=1
#     else:
#         print('Menos ...Tente mais uma vez')
#         palpite=(int(input("Qual é o seu palpite")))
#         tentativas+=1
# print("Acertou com {} tentativas".format(tentativas))



#resolução do guanabara

from random import  randint
computador= randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10. ')
print('Será que você consegue adivinhar qual foi? ')
acertou= False
palpites=0
while not acertou:
    jogador= int(input('Qual é o seu palpite '))
    palpites+=1
    if jogador== computador:
        acertou= True
    else:
        if jogador< computador:
            print('Mais... tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas.Parabens '.format(palpites))


