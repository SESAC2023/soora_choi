#q=deque() 누락
#'visited.count(True) -1'를 count.visited(True)로 잘못

#정답 #bfs
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


#👑멘토님 #dfs
import sys
from collections import deque
# 재귀 함수 깊이 해제
sys.setrecursionlimit(int(1e6))
# 입력이 10만 줄 이상일 때, 빠르게 입력 받기 위해 사용
input = sys.stdin.readline

# 노드의 개수(n)
n = int(input())
# 간선의 개수(m)
m = int(input())

# 인접 리스트
graph = [[] for i in range(n + 1)]
# 각 노드에 대한 방문 여부
visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0


def dfs(x):
    global cnt
    # 현재 노드 방문 처리
    visited[x] = True
    cnt += 1
    # 인접한 노드 하나씩 확인
    for y in graph[x]:
        # 방문하지 않았다면, 스택에 넣기
        if not visited[y]:
            dfs(y)


dfs(1)
print(cnt - 1)
