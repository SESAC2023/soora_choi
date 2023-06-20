a=int(input())
if a%4==0 and a%100!=0 :
  print(1)
elif a%400==0 :
  print(1)
else:
  print(0)

#해석해서 100,400 다른 줄로 넣었

#말그대로
a=int(input())
if a%4==0 and (a%100!=0 or a%400==0):
  print(1)
else:
  print(0)
