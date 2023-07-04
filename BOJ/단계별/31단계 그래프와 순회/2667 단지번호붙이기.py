#출력초과
import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e6))


n = int(input())

#나
graph = [ [0]*n for i in range (n) ]

for i in range(n):
  line = input()
  for j in range(n):
    graph[i][j] = int( line[j] ) 
    #라인에 있는 값 하나하나 꺼내서 자리에 넣

print(graph)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited= [ [False]*n for i in range(n) ]


def dfs(x,y):
  global cnt
  visited[x][y] = True
  cnt += 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx>=0 and ny>=0 and nx<n and ny<n:
      if visited[nx][ny]==False and graph[nx][ny]==1 :
        dfs(nx,ny)

cnt = 0
home = 0
count = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and visited[i][j] == False :
      dfs(i,j)
      count.append(cnt)
      cnt = 0
      home += 1

print (home)
print ( len(count) )
for i in count:
  print(i)
