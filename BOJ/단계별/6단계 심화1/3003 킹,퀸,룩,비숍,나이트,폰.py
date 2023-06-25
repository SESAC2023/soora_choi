data=list(map(int, input().split()))

ch=[1, 1, 2, 2, 2, 8]
ans=[0]*6

for i in range (6):
  ans[i]=ch[i]-data[i]

print(*ans)

#ans=[] ans.append=ch[i]-data[i]는 왜 안됐는지
