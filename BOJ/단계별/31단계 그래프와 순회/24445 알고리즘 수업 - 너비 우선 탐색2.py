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
    graph[i].sort(reverse=True) # 오름차순 방문

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
