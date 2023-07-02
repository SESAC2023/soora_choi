#멘토님
# 무방향 그래프(양방향 간선)
# 노드(정점)의 개수가 100,000개
# 간선(도로)의 개수가 200,000개
# BFS: 시간 복잡도 O(V+E)

import sys
from collections import deque
# 재귀 함수 깊이 해제
sys.setrecursionlimit(int(1e6))
# 입력이 10만 줄 이상일 때, 빠르게 입력 받기 위해 사용
input = sys.stdin.readline

# 노드의 개수(n), 간선의 개수(m), 시작 노드(r)
n, m, r = map(int, input().split())

# 인접 리스트
graph = [[] for i in range(n + 1)]
# 각 노드에 대한 방문 여부
visited = [False] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    # 양방향 간선이기 때문에
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort() # 오름차순 방문

# 시작할 때
q = deque()  # 큐를 생성
q.append(r)  # 큐에 시작 노드 넣기
visited[r] = True  # 시작 노드 방문 처리

answer = [0] * (n + 1)  # 각 노드를 방문한 순서
order = 1

# 큐가 빌 때까지 반복
while q:
    # 매번 큐에서 원소 꺼내기
    x = q.popleft()
    answer[x] = order  # 순서 기입
    order += 1
    # 인접한 노드 확인하기
    for y in graph[x]:
        # 방문하지 않았다면
        if not visited[y]:
            visited[y] = True
            q.append(y)

for i in range(1, n + 1):
    print(answer[i])



#트라이
import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e6))
from collections import deque

n, m, r = map(int, input().split())

graph = [ [] for i in range(n+1) ]
visited = [ [False] * (n+1) ]
visitnum = [0] * (n+1)
#num = 1

for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort()
  
q=deque()

#dfs에서 dfs(r) dfs에 r 넣어주는 대신, q에 첫값 넣어주는걸로 시작
q.append(r)
#visited[r]=True #dfs에서는 def 내부에 #??없어도 되는거 아닌가
num=1

while q:
  x=q.popleft() #x에는 pop된 거 저장, q에는 남은 리스트가 저장
  visited[x] = True #x=q.popleft 뒤에 와야쥥 #여기서 아예 없애고 if뒤에 가면? 첫번 밖에서 True 해놓으면 if 뒤로 빠져도 괜찮?
  visitnum[x] = num
  num+=1  
  for i in graph[x]:
    if not visited[i]:
      q.append(i)

#인접노드 graph로 저장해놓고 graph에 있는거 털어쓰는건 똑같은데, 인접노드 요소들을 미방문이면 q에 넣는데 오른쪽으로 쌓고 왼쪽부터 꺼내쓰다보니까 바로바로 깊이탐색으로 한 라인 노드 쓰는게 아니라, 걔네는 뒤에 누적해놓고, 앞에 들어왔던 애들부터 처리.
  
for i in range (1,n+1):
  print(visitnum[i])


#교정
