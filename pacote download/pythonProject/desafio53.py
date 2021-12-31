# frase= str(input('Digite uma frase: ')).strip().upper()
# palavras = frase.split()
# junto= ''.join(palavras)
# inverso=''
# for letra in range(len(junto)-1,-1,-1):
#     inverso+= junto[letra]
# print('O inverso de {} é {}'.format(junto,inverso))
# print(junto,inverso)
# if inverso==junto:
#     print('temos um palindromo')
# else:
#     print('A frase digitada não é um palindromo')


# outra maneira de resolver o problema
frase= str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto= ''.join(palavras)

inverso= junto[::-1]
print('O inverso de {} é {}'.format(junto,inverso))
print(junto,inverso)
if inverso==junto:
    print('temos um palindromo')
else:
    print('A frase digitada não é um palindromo')