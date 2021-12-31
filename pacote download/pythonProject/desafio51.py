print('=='*20)
print('10 TERMOS DE UM PA')
print('=='*20)



p = int(input('Primeiro termo: '))
r = int(input('Razão:',))
decimo= p+ (10-1)* r
for c in range (p,decimo+r,r):
    print(c,end='->')
print('Acabou')












print('=='*20)
print('10 TERMOS DE UM PA')
print('=='*20)


t=int(input('Primeiro termo: '))
r=int(input('Razão:  '))
decimo=t+(10-1)*r
for c in range (t,decimo+r,r):
    print(c,end=' ')