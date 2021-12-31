# from time import sleep
# quantidademulheres=0
# quantidadehomens=0
# maisvelho=0
# maisnovo=0
# menorque20=0
# somaidade=0
# mediaidade=0
#
# for q in range (1,4):
#  print('-'*10,'{}º Pessoa'.format(q),'-'*10)
#  nome=str(input('Nome:'))
#  idade= float( input('Idade: '))
#  sexo=input('Sexo[M/F]:')
#  somaidade+=idade
#  mediaidade+=somaidade/4
#
#
#  if q==1 and sexo=='m' :
#   maisvelho=idade
#   maisnovo=idade
#
#  if sexo=='f'and idade<=20:
#    quantidademulheres+=1
#
#
#  else:
#   if idade > maisvelho and sexo=='m':
#     maisvelho=idade
#   if sexo == 'f' and idade<=20:
#      quantidademulheres += 1
#
#   if idade < maisnovo and sexo=='m':
#      maisnovo=idade
#   if sexo=='f' and idade<= 20:
#       quantidademulheres += 1
#
#
#
# print('O homem mais velho tem {} anos e se chama {}'.format(maisvelho,nome))
# print('A média de idade do grupo é {}'.format(mediaidade))
# print('Ao todo são {} mulheres com menos de 20 anos'.format(quantidademulheres))



# solução do guanabara

somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=0
totmulher20=0
for p  in range(1,5):
    print('----- {}ª PESSOA -----'.format(p))
    nome= str(input('Nome')).strip()
    idade=int(input('IDADE: '))
    sexo=str(input('SEXO: [M/F]')).strip()
    somaidade+=idade
    if p==1 and  sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome

    if sexo in 'Mm' and idade> maioridadehomem:
        maioridadehomem=idade
        nomevelho= nome
    if idade < 20 and sexo in 'Ff':
        totmulher20+=1



mediaidade+=somaidade/4
print('A média e idade do grupo é {} '.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))


