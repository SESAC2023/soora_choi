import sys
n=int(input())
score=list(map(int, sys.stdin.readline().split()))

M=max(score)
sum=0

for i in range(n):
  score[i]=score[i]/M*100
  sum=sum+score[i]

print(sum/n)
