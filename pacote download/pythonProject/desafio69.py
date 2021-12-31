print("-="*20)
print("CADASTRE UMA PESSOA")
print("--"*20)
cont=0
mulheres=0
total=0
homens=0
while True:
    idade=int(input("IDADE"))
    total+=1
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input("Sexo [M/F] ")).strip().upper()[0]
        if sexo=='F':
            if idade<20:
                mulheres+=1
        else:
            if sexo=='M':
                homens+=1




    resp=' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp=='N':
        break
print(f'Total de pessoas com mais de 18 anos:{total}')
print('Ao total temos {} homens cadastrados '.format(homens))
print("E temos {} mulheres com menos de 20 anos".format(mulheres))
















# feminino=0
# masculino=0
# tot18=0
# while True:
#     idade = int(input("Idade"))
#
#     sexo=" "
#     while sexo not in 'MF':
#         sexo= str(input("Sexo [M/F] ")).strip().upper()[0]
#     if idade>=18:
#         tot18+=1
#     if sexo=='M':
#         masculino+=1
#     else:
#         if idade<20:
#             if sexo=='F':
#                 feminino+=1
#
#
#     resp=' '
#     while resp not in'SN':
#         resp=str(input("Quer continuar?[S/N] ")).strip().upper()[0]
#     if resp =='N':
#         break
#
#
#
# print("Acabou")
# print("Total de pessoas com mais de 18 anos {}".format(tot18))
# print('Ao todo temos {} homem cadastrado'.format(masculino))
# print('E temos {} mulheres com menos de 20 anos'.format(feminino))










