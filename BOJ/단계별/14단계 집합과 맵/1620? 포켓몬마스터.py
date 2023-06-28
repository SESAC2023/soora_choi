#시간초과
import sys
n,m=map(int,sys.stdin.readline().split())
N=[]
M=[]

for i in range(n):
    N.append(sys.stdin.readline().rstrip())
for i in range(m):
    M.append(sys.stdin.readline().rstrip())
   
for i in range(m):
  if M[i] in N:
    print (i)
  else:
    print (N[i])
