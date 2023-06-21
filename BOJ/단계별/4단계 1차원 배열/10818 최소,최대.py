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
