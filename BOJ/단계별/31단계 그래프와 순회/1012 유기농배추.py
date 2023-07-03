#수정
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]


def dfs(x, y):
  visited[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and ny >= 0 and nx < m and ny < n:
      if graph[nx][ny] == 1: #안 넣어서 전체기 트루됏
        if not visited[nx][ny]:
          dfs(nx, ny)


tc = int(input())
for i in range(tc):
  m, n, k = map(int, input().split())
  graph = [[0] * n for i in range(m)]  #m,n 으로 했을 때 범위 오류 떠서 바꿈.
  visited = [[False] * n for i in range(m)]
  for i in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

  ans = 0

  for i in range(m):  # 싹 tc안으로 넣
    for j in range(n):
      if graph[i][j] == 1 and visited[i][j] == False:
        ans += 1
        dfs(i, j)
  print(ans)
