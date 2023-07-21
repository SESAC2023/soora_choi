#런타임 에러
a,b = map(int, input().split())
alist = []
blist = []

for i in range(a):
  line=input().split()
  current=[]
  for x in line:
    current.append(int(x))
  alist.append(current)

for i in range(b):
  line=input().split()
  current=[]
  for x in line:
    current.append(int(x))
  blist.append(current)

sum=[[0]*b for i in range(a)]
for i in range(a):
  for j in range(b):
    sum[i][j]=alist[i][j]+blist[i][j]

for i in (sum):
  print(*i)


#주영님
N, M = map(int,input().split())

A, B = [], []

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)

for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j], end= ' ')
    print()


#진호님
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
data1 = []
data2 = []

for i in range(1, 2*N+1):  # 입력 받는 것 때문에 계속 틀렸었음. 여기가 중요
    if i > N:
        data2.append(list(map(int, sys.stdin.readline().rstrip().split())))
    else:
        data1.append(list(map(int, sys.stdin.readline().rstrip().split())))
      
for j in range(N):
    for k in range(M):
        print(data1[j][k]+data2[j][k], end=' ')
    if j<N-1:  
        print()
