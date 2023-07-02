#멘토님
"""
1) 내용 훑기: 그래프, DFS, 방문 처리, 탐색
2) (중요) 입력 조건:
  - 노드(도시) 혹은 정점 개수 최대 100,000개 #시간복잡도nlogn
  - 간선(도로) 개수 최대 200,000개 
3) 문제 아이디어 생각하기
  - DFS로 풀면 되지 않을까?
  - DFS의 시간 복잡도가 O(N + M)이니까, 단순 DFS 돌리면 시간 초과 X => 단순 DFS ok
4) 코드 작성
"""

#두고 쓸 코드 (재귀 깊이 한도 해제, 빠른 입력받기)
import sys
sys.setrecursionlimit(int(1e6))
sys.stdin.readline


# 정점 개수(N), 간선 개수(M), 시작 노드(R)
n, m, r = map(int, input().split())

graph = [[] for i in range(n + 1)]
"""
graph = [
    [],
    [],
    ...
    []
]
"""

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
"""
graph = [
    [],
    [4, 2],
    [1, 3, 4],
    [2, 4],
    [1, 2, 3],
    []
]
"""

for i in range(1, n + 1):
    graph[i].sort()
"""
graph = [
    [],
    [2, 4],
    [1, 3, 4],
    [2, 4],
    [1, 2, 3],
    []
]
"""

visited = [False] * (n + 1)

# visited = [False, False, False, False, False, False]
#                     1      2      3      4      5

answer = [0] * (n + 1)


def dfs(x):
    global order
    visited[x] = True
    # print(x) # 현재 방문한 노드를 출력
    answer[x] = order  # [핵심] 노드를 방문한 "순서"를 기록
    order += 1
    # 현재 노드(x)의 인접 노드를 확인하며
    for y in graph[x]:
        # 인접 노드인 y가 아직 방문하지 않은 노드라면
        if not visited[y]:
            dfs(y)


order = 1
dfs(r)

for i in range(1, n + 1):
    print(answer[i])



#트라이
import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n, m, r = map(int, input().split())

graph=[[] for i in range(n+1)]

for i in range (m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

#graph.sorted

visitnum=[0]*(n+1)
num=0

visited=[ [False]]
#n+1유무, 2차원배열로?, 필요유무

stack=[]

def dfs (V, E, R):
  stack.append(R)
  visitnum[R]=num+1
  s=stack.pop(0)
  #s는 남은리스트? 팝된 놈?
  for i in (graph[s]):
    stack.append(i)
    if stack:
      dfs(V, E, stack[0])

  #ㅜㅜbfs 덱 popleft도 아니고..이럴리가 없는데.. 스택 선입선출하려면 append할때 순서 거꾸로 넣는 것 부터?
  #if stack:
    
dfs(n,m,r)

for i in range(1,n+1):
  print(visitnum[i])



#교정
import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n, m, r = map(int, input().split())

graph=[[] for i in range(n+1)]

for i in range (m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

#graph.sorted
##리스트 속 리스트들 각각 정렬
for i in range (n+1):
  graph[i].sort()
#자꾸 graph(i)...

visitnum=[0]*(n+1)

#num=0
##global 변수로 사용 def dfs global num
##외부에서 num=1로 저장
num=1

#visited=[ [False]]
#아리송!! n+1유무, 2차원배열로?, 필요유무 (뒤)
##n+1 로 1차원배열
visited = [False] * (n+1)

#stack=[]
##필요x. graph에 인접노드 저장해놓고 앞 원소부터 털어서 쓰는거자체가 스택

#def dfs (V, E, R):
##def dfs (x):
def dfs (R):
  
  ##global num!!
  global num
  
  visitnum[R] = num
  #visitnum[R]=num+1
  #s=stack.pop(0)
  #s는 남은리스트? 팝된 놈?
  ##
  
  #stack.append(R)
  #for i in (graph[s]):
  ##스택에 넣고 스택에서 꺼내 쓸 필요 없이, 들어온 값 R에 대해서 인접노드(graph[R])꺼내쓰면 됨
  for i in graph[R]:
    
    #stack.append(i)
    #if stack:
    #  dfs(V, E, stack[0])
    ##인접노드 i 의 방문유무에 따라
    if not visited[i]:
    ##🌟visited[i]로 사용해서 n+1로 만들어놨어야해- 입력값으로 간선 정보 주어진 값으로 graph[a].append(b) 했을 때부터 '노드'를 부를 때 1번 노드는 0번째가 아닌 1번째로 다뤄야해서 graph도 노드 관련 정보들도 다 n+1칸 만들어서 사용
    #ㅜㅜbfs 덱 popleft도 아니고..이럴리가 없는데.. 스택 선입선출하려면 append할때 순서 거꾸로 넣는 것 부터?
    #if stack:
    ##🌟스택 만들필요없이, 인접노드graph만들어 둔거에서 앞에서부터 차례대로 꺼내쓰면 되잖아!!

      
      #visitnum[i] = num + 1
      ##이렇게하면 재귀함수 들어가면서 if로 들어온 변수는 visitnum를 두 번 저장당함. num는 1씩 누적되지 않고 1,2만 반복
      num+=1
      ##멘토님은 앞으로 뺌
      
      dfs(i)


#dfs(n,m,r)
dfs(r)
##입력받은 변수 n,m,r/ 함수정의할때 쓴 변수 R -> 입력받은 변수를 함수에 넣

for i in range(1,n+1):
  print(visitnum[i])

'''
num =1

def dfs (R):
  global num
  visitnum[R] = num
  
  for i in graph[R]:
    if not visited[i]:
      visitnum[i] = num + 1
      dfs(i)

이렇게 하면 가령 인접노드로 2가 불려왔을 때
visitnum[2] = 1+1 #2를 잘 받았는데
dfs(2)로 재귀함수 들어가면서 
visitnum[2]를 또 만나는데, 그때 걍 num (=1)야..

즉, visitnum 번호 수여는 한 번만 써줘서 겹치는 일 없게 해줘야 하고, 
num +=1 을 적절한 곳에서.
-번호 수여는 방문유무 무관하게 되어야 하니까 가장 큰 앞쪽에 있는게 맞고.
-num+=1은 처음 방문인 경우 (if not visited)에만

num =1

def dfs (R):
  global num
  visitnum[R] = num
  
  for i in graph[R]:
    if not visited[i]:
      num + = 1
      dfs(i)
      
*dfs 함수에 들어오게 되는 것 자체가, 방문한적없는 값이라.. 들어온거긴해서 num+=1 위로 올려도 될듯
(방문경험 없는 애들만 들어온 후, 걔랑 인접노드 방문 경험 있는지 for i in graph[x] 에서 걸러짐)

num+=1은 if 밑에 있어도 맨위에 있어도 괜찮을듯
'''
