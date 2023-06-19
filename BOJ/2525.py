a,b=map(int, input().split())
c=int(input())

num=0

while c>60:
  c=c-60
  num=num+1

if c<=60:
  if b+c<60:
    if a+num>=24:
      print(a+num-24, b+c)
    else:
      print(a+num, b+c)
  else:
    if a+num>=23:
      print(a+num-23, b+c-60)
    else:
      print(a+num+1, b+c-60)
