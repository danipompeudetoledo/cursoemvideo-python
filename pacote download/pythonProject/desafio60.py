# numero= (int(input('''Digite um numero para
# calcular seu fatorial: ''')))
# resultado=1
# count=1
# while count<= numero:
#     resultado=resultado*count
#     count=count+1
#     print(resultado)

# numero= (int(input('''Digite um numero para
# calcular seu fatorial: ''')))
# c=1
# r=1
# while c<=numero:
#     r=r*c
#     c=c+1
#     a=c-1
#
# print("calculando {}={}x{}={}".format(numero,numero,r,r,a,a))

#solução 1 do guanabara

# from math import  factorial
# n= int(input('Digite um numero para calcular seu fatorial: '))
# f=factorial(n)
# print('o fatorial de {} é {} '.format(n,f))

#soluçao 2 do guanabara
# n = int(input('Digite um numero para calcular seu fatorial: '))
# c=n
# f=1
# print('calculando {}!='.format(n),end=' ')
# while c > 0:
#  print('{} '.format(c),end=' ')
#  print('x' if c >1 else'=',end=' ')
#  f=f*c
#  c=c-1
# print( '{}'.format(f))

n = int(input('Digite um numero para calcular seu fatorial: '))
c=n
f=1
for fatorial in range (5,1,-1):
  c-=1
  f = f*c
  print('{}'.format(c),end='')
  print('x'if c>1 else '=',end='')
  print('{}'.format(f),end='')



