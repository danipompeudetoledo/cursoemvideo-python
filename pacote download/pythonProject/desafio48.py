# from random import randint
# c=0
# for n in range (0,10,1):
#     v=randint(1,501)
#     c= c+v
# print('a soma de todos os {} valores solicitados é {}'.format(n,c) )

soma=0
cont=0
for c in range(1,500,2):
    if c % 3==0:
        cont=cont+1
        soma= soma+ c
print('a soma de todos os {} valores solicitados é {}'.format(cont,soma) )


