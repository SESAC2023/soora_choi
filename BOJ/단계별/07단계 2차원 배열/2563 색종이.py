#0,1,2,...,99칸
#100*100개의 칸에 0값 주기
list = [[0]*100 for i in range(100)]

#색종이 붙은 칸은 1값 주기
n=int(input())
for i in range(n):
  a,b=map(int, input().split())
  for i in range(b,b+10):
    for j in range(a, a+10):
      list[i][j]=1

#2차원 배열의 합
sum=0
for i in list:
  for j in i:
    sum+=j
print(sum)
