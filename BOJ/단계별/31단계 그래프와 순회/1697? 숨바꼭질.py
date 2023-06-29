#while문에서 새로 들어오는 값 범위 제한 주는 방식 다르게 하면 메모리 초과

#정답
import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input=sys.stdin.readline

n,k = map(int, input().split())

visited = set()
distance = dict()

q=deque()
q.append(n)
visited.add(n)
distance[n]=0

while q:
  x = q.popleft()
  if x == k:
    break
  nx = x + 1
  if nx>=0 and nx<=100000:
    if nx not in visited:
      visited.add(nx)
      distance[nx]=distance[x]+1
      q.append(nx)
  nx = x - 1
  if nx>=0 and nx<=100000:
    if nx not in visited:
      visited.add(nx)
      distance[nx]=distance[x]+1
      q.append(nx)
  nx = 2*x
  if nx>=0 and nx<=100000:
    if nx not in visited:
      visited.add(nx)
      distance[nx]=distance[x]+1
      q.append(nx)
      
print(distance[k])    



#메모리초과
import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input=sys.stdin.readline

n,k = map(int, input().split())

visited = set()
distance = dict()

q=deque()
q.append(n)
visited.add(n)
distance[n]=0

while q:
  x = q.popleft()
  if x == k:
    break
  nx = x + 1
  if nx<0 or nx>100000:
      pass
  if nx not in visited:
      visited.add(nx)
      distance[nx]=distance[x]+1
      q.append(nx)
  nx = x - 1
  if nx<0 or nx>100000:
      pass
  if nx not in visited:
      visited.add(nx)
      distance[nx]=distance[x]+1
      q.append(nx)
  nx = 2*x
  if nx<0 or nx>100000:
      pass
  if nx not in visited:
      visited.add(nx)
      distance[nx]=distance[x]+1
      q.append(nx)
      
print(distance[k])    




#멘토님
"""
BFS: 최단 거리를 탐색할 때 사용할 수 있음.
  조건: "단, 모든 간선의 비용이 동일할 때만"
"""

from collections import deque

# 출발 위치(n), 도착 지점(x)를 입력받기
n, x = map(int, input().split())

visited = set()  # 방문 여부
distance = dict()

q = deque()
q.append(n)  # n을 큐에 삽입
visited.add(n)  # n을 방문 처리
distance[n] = 0  # 자기 자신까지는 0초가 걸림

# BFS 수행
while q:  # 큐가 빌 때까지 반복
    current = q.popleft()  # 큐에서 원소 추출
    # print(current)
    # -1, +1 혹은 *2가 있음
    next = current - 1
    if next not in visited:  # 방문한 적 없다면 최단 거리 기록
        if next >= 0 and next <= 100000:
            visited.add(next)
            q.append(next)
            distance[next] = distance[current] + 1
    next = current + 1
    if next not in visited:  # 방문한 적 없다면 최단 거리 기록
        if next >= 0 and next <= 100000:
            visited.add(next)
            q.append(next)
            distance[next] = distance[current] + 1
    next = current * 2
    if next not in visited:  # 방문한 적 없다면 최단 거리 기록
        if next >= 0 and next <= 100000:
            visited.add(next)
            q.append(next)
            distance[next] = distance[current] + 1

print(distance[x])
