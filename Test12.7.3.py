per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Сумма вклада"))
TKB = int(money/100 * per_cent.get('ТКБ'))
SKB = int(money/100 * per_cent.get('СКБ'))
VTB = int(money/100 * per_cent.get('ВТБ'))
SBER = int(money/100 * per_cent.get('СБЕР'))
print(' deposit =',[TKB,SKB,VTB,SBER])
MAX = max(TKB,SKB,VTB,SBER)
print("max deposit =",[MAX])

#или так
money_a = input("Сумма вклада")
b = list(per_cent.values())
c = int(money_a)
print(' deposit =',[int(c*0.01 * b[0]),int(c*0.01 * b[1]) ,int(c*0.01 * b[2]),int(c*0.01 * b[3])])
MAXx = max([int(c/100 * b[0]),int(c/100 * b[1]) ,int(c/100 * b[2]),int(c/100 * b[3])])
print("max deposit =",MAXx)