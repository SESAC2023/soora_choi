#세 개짜리 리스트에 넣고 리스트합 기준으로 넣고 뺴고... X

a,b=map(int, input().split())
list=list(map(int, input().split()))

'''
for i in range(b):
  for j in range(i+1, b):
    for k in range(j+1, b):
      sum=
      '''
#값이 아니라 번쨰로 나눔
max=0
for i in range(a):
  for j in range(i+1, a):
    for k in range(j+1, a): #a=5, j=4면 k=??
      sum=list[i]+list[j]+list[k]
      if sum <= b and max<sum:
        max=sum
print(max)



#주영님
N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M and max_sum < sum:
                max_sum = sum

print(max_sum)


#다솔님
# 카드를 3장 뽑는 모든 경우의 수 구해서 조건 비교
n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for i in range(n-2):
  c1 = cards[i]
  for j in range(i+1, n-1):
    c2 = cards[j]
    for k in range(j+1, n):
      c3 = cards[k]
      s = c1 + c2 + c3
      if s >= max_sum and s <= m:
        max_sum = s
print(max_sum)
