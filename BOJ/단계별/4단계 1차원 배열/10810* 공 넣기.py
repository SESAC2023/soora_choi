N,K=map(int, input().split())
t=[]
ans=[0]*N

for i in range(K):
  arr=list(map(int, input().split()))
  t.append(arr)

for i in (t):
  for j in range(1,N+1):
    if j>=i[0] and j<=i[1]:
      ans[j-1]=i[2]

for p in ans:
  print (p, end=" ")

#print(ans): 로 해서 리스트로 나왔었음
