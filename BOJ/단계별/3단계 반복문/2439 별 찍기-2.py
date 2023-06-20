n=int(input())
for i in range(1,n+1):
  print(' '*(n-i)+'*'*i)

#오답 (n이 5일 때까지만 적용됨)
n=int(input())
for i in range(n):
  x= "%5s" %('*'*(i+1))
  print(x)
  
