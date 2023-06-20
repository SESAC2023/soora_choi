import sys
t=int(input())

data = sys.stdin.readline

for i in range (t):
  a,b=map(int, data().split())
  print(a+b)
