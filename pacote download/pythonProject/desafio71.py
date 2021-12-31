# print('='*40)
# print('{:^40}'.format(' Banco CEV '))
# print('='*40)
#
#
# valor=int(input('Qual valor você quer sacar R$ '))
# total=valor
# ced=50
# totced=0
#
# while True:
#     if total >= ced:
#         total-=ced
#         totced+=1
#
#     else:
#         print("total de cedulas é de {} de {}".format(totced, ced))
#         if ced==50:
#             ced=20
#         elif ced==20:
#             ced=10
#         elif ced==10:
#              ced=1
#         totced=0
#
#         if total==0:
#                 break
#
#


print("="*40)
print('{:^40}'.format('BANCO CEV'))
print("="*40)


valor=int(input("que valor vocÇe quer sacar? "))
totced=0
ced=50
total=valor


while True:
    if total>=ced:
        total-=ced
        totced+=1
    else:
        print('total de cedulas é {} de R$ {}'.format(totced,ced))
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=5
        totced=0
        if total==0:
             break
































