# menor=0
# maior=0
# valor = list()
# for v in range (0,5):
#     valor.append(int(input(f'Digite uma valor para a posição {v} : ')))
#     if v==0:
#         maior=menor=valor[v]
#     else:
#         if valor[v] > maior:
#             maior=valor[v]
#         if valor[v]< menor:
#             menor=valor[v]
#
#
# print(f'Você digitou os valores {valor}')
#
#
# print(f'O maior valor digitado foi {maior} nas posições ', end='')
# for i,v in enumerate(valor):
#     if v == maior:
#         print(f'{i}...',end='')
# print()
#
# print(f'O menor valor digitado foi {menor} nas posições ', end='')
# for i,v in enumerate(valor):
#     if v== menor:
#         print(f'{i}...',end='')
# print()
#
#
#
menor=0
maior=0
valor=[]
for v in range(0,2):
      valor.append(int(input(f'Digite uma valor para a posição {v}: ')))
      if v==0:
         maior=menor=valor[v]

      else:
       if valor[v]> maior:
           maior= valor[v]
       if valor[v]< menor:
          menor = valor[v]

print(f"Você digitou os valores {valor} ")

print(f'O MAIOR VALOR É {maior} nas posições ', end='')
for c,v in enumerate(valor):
    if v==maior:
        print(f' {c}... ',end='')

print()
print(f'O menor valor é {menor} nas posições nas posições ', end='')
for c,v in enumerate(valor):

        if v==menor:
            print(f' {c}...',end='')
print()





























