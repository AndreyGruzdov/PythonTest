per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Сумма вклада"))
tbk = int(money/100 * per_cent.get('ТКБ'))
skb = int(money/100 * per_cent.get('СКБ'))
vtb = int(money/100 * per_cent.get('ВТБ'))
sber = int(money/100 * per_cent.get('СБЕР'))
print(' deposit =',[tbk,skb,vtb,sber])
max_m = max(tbk,skb,vtb,sber)
print("max deposit =",[max_m])

#или так
money_a = input("Сумма вклада")
b = list(per_cent.values())
c = int(money_a)
print(' deposit =',[int(c*0.01 * b[0]),int(c*0.01 * b[1]) ,int(c*0.01 * b[2]),int(c*0.01 * b[3])])
max_mm = max([int(c/100 * b[0]),int(c/100 * b[1]) ,int(c/100 * b[2]),int(c/100 * b[3])])
print("max deposit =",max_mm)