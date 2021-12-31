times=('curica','parmera','santos', 'gremio','cruzeiro', 'flamengo','vasco','chape','atletico-pr','bahia',
       'são Paulo', 'avai', 'ponte',
       'atletico-go', 'bahia','atletico','botafogo', 'fluminense','ec vitoria','sport')


print('{:^40}'.format(' TIMES DO BRASILIRÃO '))
print('Lista de times do Brasileirão {}'.format(times))
print('-='*20)

print('Os 5 primeiros são: {}' .format(times[0:5]))
print('-='*20)

print('Os 4 ultimos são:{}'.format(times[-4:]))
print('-='*20)

print("Times em ordem alphabética {}".format(sorted(times)))
print('-='*20)

print('A {} está na {}ª posição'.format(times[7],times.index('chape')+1))


#-------------------------------------------------------
# for t in times:
#        print(t)
