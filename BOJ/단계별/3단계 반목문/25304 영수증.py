total=int(input())
num=int(input())
sum=0

for i in range(num):
  a,b=map(int, input().split())
  sum=sum+a*b

if sum==total:
  print("Yes")
else:
  print("No")

#빼줘서 0인지 확인하는 방법도
