n=0
cont=0



while True:
    n = int(input("Quer ver a tabuada de qual valor? "))



    for c in range(1,11):
     cont += 1
     r = n * cont
     print('{} x {} = {} '.format(n, c, r))








print('-' * 20)



