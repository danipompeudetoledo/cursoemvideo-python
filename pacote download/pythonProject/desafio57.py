# sexo='m/f'

# sexo = str(input('Informe seu sexo:[M/F]: ')).upper().strip()[0]
# while sexo !='M' and  sexo!='F':
#
#   sexo=(str(input('Dados inválidos. Por favor, informe seu sexo: '))).upper()
# print('Sexo {} registrado com sucesso'.format(sexo))


#resolução do guanabara

sexo= str(input("Informe seu sexo: [M/F]")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo=str(input("Dados inválidos. Por favor informe seu sexo: ")).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

