# palavra= ('Aprender','Programar','linguagem','Python','curso','Gratis','Estudar','Praticar','Trabalhar',
#           'Mercado','Programador','Futuro')
# for p in palavra:
#
#      print(f'\nNa palavra {p} temos',end=' ')
#      for letra in p:
#          if letra.lower() in 'aeiou':
#              print(letra, end=' ')


















palavra= ('Aprender','Programar','linguagem','Python','curso','Gratis','Estudar','Praticar','Trabalhar',
          'Mercado','Programador','Futuro')
for p in palavra:
 print(f' \nPara cada palavra {p} temos ',end='')
 for letra in p:
     if letra.lower() in 'aeiou':
         print(letra,end='')