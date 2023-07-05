#시간->bfs

import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e6))
from collections import deque

m,n = map(int, input().split())
graph = [ []*m for i in range (n)]
visited = [ [False]*m for i in range(n) ]
visitnum = [ [0]*m for i in range(n) ]

for i in range(n):
  graph[i].append( list (map(int, input().split())) )
  #graph[i].append(int(input().split())) #append()에 리스트가 들어갈 수 없다 
  #아니 그게 아니라 int()에 리스트 못 들어가.... string 문자열만
  #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
  #for j in range(m): #graph[i][j]= 요런것도 놉
  #한줄씩 입력 받을거고, 그 줄의 요소들이 한 리스트에 들어가고, 그 리스트들이 전체 리스트에 들어가야 해
  ##int(input().split) - 한 줄씩, 각 요소 잘 찢어서 받았음 -> 바로 리스트화?: list ( int(input().split()) )
print(graph)

q = deque()
cnt = 0

dx= [0, 0, 1, -1]
dy= [1, -1, 0, 0]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and visited[i][j] == False:
      q.append (i,j)
      while q:
        x,y=q.popleft()
        visitnum[x][y] = cnt
        cnt += 1
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if nx>=0 and ny>=0 and nx<n and ny<m:          
            if visited[nx][ny]==False and graph[nx][ny] ==0 :
              visited[nx][ny] == True
              graph[nx][ny] == 1
            

print ( max(visitnum) )
