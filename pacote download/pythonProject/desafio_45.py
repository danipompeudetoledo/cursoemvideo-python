from random import randint
from time import sleep

itens= ['Pedra','Papel','Tesoura']
computador= randint(0,2)
print('''Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador=int(input('Qual é a sua jogada? '))
print('-='*11)


print('JO')
sleep(1)


print('KEN')
sleep(1)


print('PO')
sleep(1)

print('-='*11)

print('O jogador jogou {}'.format(itens[jogador]))

print('O computador Jogou  {}'.format(itens[computador]))
print('-='*10)

if computador == 0: #computador jogou pedra
    if jogador == 0:
     print('Empate')
    elif jogador==1:
     print('Jogador venceu')
    elif jogador==2:
       print('Computador venceu')
    else:
       print('Jogada inválida')


elif computador==1: #computador jogou papel
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate')

    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('Jogada inválida')
elif computador==2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Compútador venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')






