
# extenso=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
#
# numero = int(input('Digite um número entre 0 e 20: '))
#
# while numero not in range(0, 20):
#  numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
#
#
# else:
#  print(f'Você digitou  o numero  {extenso[numero]}')




extenso=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')



while True:
 numero = int(input('Digite um número entre 0 e 20: '))
 if 0<= numero <=20:
   break
 print('Tente novamente.',end='')
print(f'Você digitou o numero {extenso[numero]}')