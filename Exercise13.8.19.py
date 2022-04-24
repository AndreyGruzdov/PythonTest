free = 0
lait= 990
full = 1390
age18 = 0
age18_25 = 0
agd25 = 0
a = int(input("Введите количество билетов"))
for c in range(1,a+1):
  b = (int(input("Введите возраст")))
  if b <=18:
     age18 += 1
  elif 18 < b <=25:
     age18_25 += 1
  else:
    b < 25
    agd25 += 1
if a <=3:
  S =float (age18*free+age18_25+lait+agd25*full)
  print("Полная стоимость =",S)
else:
  S = float ((age18*free+age18_25+lait+agd25*full)- (age18*free+age18_25+lait+agd25*full)/100*10)
  print("Стоимость =", S, "скидка 10%")

