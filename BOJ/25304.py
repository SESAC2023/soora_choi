total=int(input())
num=int(input())
sum=0

for i in range(num):
  a,b=map(int, input().split())
  sum=sum+a*b

if sum==total:
  print("YES")
else:
  print("NO")
