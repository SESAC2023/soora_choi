import sys

n,x = map(int, sys.stdin.readline().split())
arr=list(map(int, sys.stdin.readline().split()))

for i in (arr):
  if i<x:
    print(i)


#멘토님
n, x = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] < x:
        print(arr[i], end=" ")
