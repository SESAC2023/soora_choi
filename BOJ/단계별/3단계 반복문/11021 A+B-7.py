import sys

t=int(input())

for i in range (t):
  a,b=map(int, input().split())
  print("Case #" + str(i+1) + ": " + str(a+b))

  print(f"Case #{i+1}: {a+b}")
