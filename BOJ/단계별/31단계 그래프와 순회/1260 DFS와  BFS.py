#👑멘토님
import sys
from collections import deque
# 재귀 함수 깊이 해제
sys.setrecursionlimit(int(1e6))
# 입력이 10만 줄 이상일 때, 빠르게 입력 받기 위해 사용
input = sys.stdin.readline

# 정점의 개수(n), 간선의 개수(m), 시작 정점(v)
n, m, v = map(int, input().split())

graph = [[] for i in range(n + 1)]  # 그래프
visited = [False] * (n + 1)  # 방문 처리 배열

for i in range(m):
    x, y = map(int, input().split())
    # 양방향 간선
    graph[x].append(y)
    graph[y].append(x)

# 방문할 때는 오름차순으로 방문
for i in range(1, n + 1):
    graph[i].sort()


def dfs(x):
    visited[x] = True  # 방문 처리
    print(x, end=" ")
    for y in graph[x]:  # 인접한 노드
        # 방문 안 했다면 스택에 넣기
        if not visited[y]:
            dfs(y)


dfs(v)
print()

# 이제 BFS 수행하기
visited = [False] * (n + 1)  # (중요) 방문 처리 배열
q = deque()  # 큐 만들기
visited[v] = True  # 시작 노드 방문 처리
q.append(v)  # 시작 노드 큐에 넣기
"""
graph[1] = [2, 3, 4]
graph[2] = [1, 4]
graph[3] = [1, 4]
graph[4] = [1, 2, 3]
"""

while q:  # 큐가 빌 때까지 반복
    x = q.popleft()
    print(x, end=" ")
    for y in graph[x]:  # 인접 노드 확인
        if not visited[y]:
            visited[y] = True
            q.append(y)


#🥹정답
import sys
sys.setrecursionlimit(int(1e6))
from collections import deque
input=sys.stdin.readline

n, m, r = map(int, input().split())

graph = [ [] for i in range(n+1) ]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
for i in range (n+1):
  graph[i].sort()


#dfs
visited = [False] * (n+1)
def dfs(x):
  visited[x]=True #if 밑으로 넣고 1항 따로 해줄까하다가

  print(x, end=' ')
  for i in graph[x]:
    if not visited[i]:
      dfs(i)

dfs(r) #이렇게 시작하는거 생각하니까 dfs 안에서 첫번째도 해결하는게 좋을 것 같은
print()

#bfs
visited = [False] * (n+1)
q=deque()
q.append(r)
visited[r]=True

while q: 
  x=q.popleft()
  print(x, end=' ')
  for i in graph[x]:
    if not visited[i]:
      visited[i]=True
      q.append(i)


#❌try2
#오름차순 누락
import sys
sys.setrecursionlimit(int(1e6))
from collections import deque
input=sys.stdin.readline

n, m, r = map(int, input().split())

graph = [ [] for i in range(n+1) ]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

#dfs
visited = [False] * (n+1)
def dfs(x):
  visited[x]=True #if 밑으로 넣고 1항 따로 해줄까하다가

  print(x, end=' ')
  for i in graph[x]:
    if not visited[i]:
      dfs(i)

dfs(r) #이렇게 시작하는거 생각하니까 dfs 안에서 첫번째도 해결하는게 좋을 것 같은
print()

#bfs
visited = [False] * (n+1)
q=deque()
q.append(r)
visited[r]=True

while q: 
  x=q.popleft()
  print(x, end=' ')
  for i in graph[x]:
    if not visited[i]:
      visited[i]=True
      q.append(i)



#❌try2
#예제2 출력값이 다르게 나옴
import sys
sys.setrecursionlimit(int(1e6))
from collections import deque
input=sys.stdin.readline

n, m, r = map(int, input().split())

graph = [ [] for i in range(n+1) ]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

#dfs
visited = [False] * (n+1)
#dfsvisit = [0] * (n+1)
#num =1

def dfs(x):
  #global num
  visited[x]=True #if 밑으로 넣고 1항 따로 해줄까하다가
  #dfsvisit[x]=num
  #num+=1
  print(x, end=' ')
  for i in graph[x]:
    if not visited[i]:
      dfs(i)

dfs(r) #이렇게 시작하는거 생각하니까 dfs 안에서 첫번째도 해결하는게 좋을 것 같은
print()

#print ( *dfsvisit[1:] ) #아오.. 이거 식으로 어떻게?

#bfs
visited = [False] * (n+1)
#bfsvisit = [0] * (n+1)
q=deque()
q.append(r)
visited[r]=True
#bfsvisit[r]=1

#nums=1

while q: #글로벌 지움
  x=q.popleft()
  #bfsvisit[x]=nums #num 로 했다가 누적당함
  #nums+=1
  print(x, end=' ')
  for i in graph[x]:
    if not visited[i]:
      visited[i]=True
      q.append(i)

#for i in bfsvisit: #입력부분 print i in range print bfsvisit[i]
#print( *bfsvisit[1:] )


#❌try1 
#방문한 순서대로 출력한 게 아니라, 각 노도의 방문순서(distance)를 출력했다.
import sys
sys.setrecursionlimit(int(1e6))
from collections import deque
input=sys.stdin.readline

n, m, r = map(int, input().split())

graph = [ [] for i in range(n+1) ]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

#dfs
visited = [False] * (n+1)
dfsvisit = [0] * (n+1)
num =1

def dfs(x):
  global num
  visited[x]=True #if 밑으로 넣고 1항 따로 해줄까하다가
  dfsvisit[x]=num
  num+=1
  for i in graph[x]:
    if not visited[i]:
      dfs(i)

dfs(r) #이렇게 시작하는거 생각하니까 dfs 안에서 첫번째도 해결하는게 좋을 것 같은

print ( *dfsvisit[1:] ) #아오.. 이거 식으로 어떻게?

#bfs
visited = [False] * (n+1)
bfsvisit = [0] * (n+1)
q=deque()
q.append(r)
visited[r]=True
bfsvisit[r]=1

nums=1

while q: #글로벌 지움
  x=q.popleft()
  bfsvisit[x]=nums #num 로 했다가 누적당함
  nums+=1
  for i in graph[x]:
    if not visited[i]:
      visited[i]=True
      q.append(i)

#for i in bfsvisit: #입력부분 print i in range print bfsvisit[i]
print( *bfsvisit[1:] )
