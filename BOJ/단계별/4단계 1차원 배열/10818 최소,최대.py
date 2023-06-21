n=int(input())
arr=list(map(int,input().split()))

b=arr[0]
c=arr[0]

for i in (arr):
  b=max(b,i)
for i in (arr):
  c=min(c,i)
  
print(c,b)

#b=arr[0], c=arr[0] 를 for문 안에 넣으면 최대최소 담던 b,c변수가 자꾸 초기화 돼

#멘토님
n = int(input())
arr = list(map(int, input().split()))

min_value = 1e9 # 일단 무지막지하게 큰 값
max_value = -1e9 # 일단 무지막지하게 작은 값

for i in range(n):
    # 현재 원소가 현재까지의 min_value보다 작다면
    if arr[i] < min_value:
        min_value = arr[i] # 갱신
    # 현재 원소가 현재까지의 max_value보다 크다면
    if arr[i] > max_value:
        max_value = arr[i] # 갱신

print(min_value, max_value)
