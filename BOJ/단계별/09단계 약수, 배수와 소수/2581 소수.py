s=int(input())
b=int(input())
list=[]

for n in range(s, b+1): #60~100
  list.append(n)
  for i in range(2,n): #n은 소수인가?
    if n%i == 0:
      if n in list:
        list.remove(n)

if list == True:
  sum=0
  for i in list:
    sum+=i
  print(sum)
  print(list[0])
else:
  print(-1)
