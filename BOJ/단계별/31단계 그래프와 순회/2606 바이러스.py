#q=deque() 누락
#'visited.count(True) -1'를 count.visited(True)로 잘못


import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e6))
from collections import deque

n=int(input())
m=int(input())

graph=[ []for i in range(n+1) ]

for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False]*(n+1)

q=deque()
q.append(1)
visited[1]=True

while q:
  x=q.popleft()
  for i in graph[x]:
    if not visited[i]:
      q.append(i)
      visited[i]=True

print( visited.count(True) -1 ) 
