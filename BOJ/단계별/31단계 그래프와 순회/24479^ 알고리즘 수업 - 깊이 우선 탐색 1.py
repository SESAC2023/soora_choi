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
