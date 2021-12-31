# # num = float(input('Digite um número: '))
# #
# # c = str(input('Quer continuar? [S/N] ')).upper()
# num=0
#
# maior=0
# menor=0
# soma=0
# cont=0
# media=0
# c='sS'
#
# while c in 'sS':
#         num = int(input('Digite um número: '))
#         c = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
#         soma+= num
#         cont+=1
#
#
# media= soma/cont
#
# if cont==1:
#     maior=menor=num
# else:
#     if num> maior:
#         maior = num
#     if num < menor:
#         menor= num
#
#
#     m=num
#     media = (soma + num) / cont
#
#
#
# print('Você digitou {} numeros e a media foi {}'.format(cont,media))
# print(('o maior valor foi {} e o menor foi {}'.format(maior,menor)))


c="S"
cont=0
soma=0
maior=0
menor=0
media=0
while c in 'Ss':
    num= int(input("digite um número:"))
    c = str(input("Quer continuar? ")).upper().strip()[0]
    soma+=num
    cont+=1
media= soma/cont

if cont==1:
    maior = menor= num
else:
    if num > maior:
        maior= num
    if num < menor:
        menor = num


print("voçe digitou {} e media foi {}".format(cont,media))
print("o maior valor foi {} e menor foi {}".format(maior, menor))













