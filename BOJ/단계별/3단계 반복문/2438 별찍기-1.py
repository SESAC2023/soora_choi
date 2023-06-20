#1
n=int(input())

for i in range(1,n+1):
  print("*"*i)


#2
n=int(input())

for i in range(n):
  print("*"*(i+1))


#3 이중반복문
n=int(input())
for i in range(1, n+1):
  for j in range(i+1):
    print("*", end=" ")
  print()
