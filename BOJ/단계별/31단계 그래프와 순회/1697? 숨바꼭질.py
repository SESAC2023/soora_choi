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
