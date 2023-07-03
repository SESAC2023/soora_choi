#try2
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


#try1 
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
