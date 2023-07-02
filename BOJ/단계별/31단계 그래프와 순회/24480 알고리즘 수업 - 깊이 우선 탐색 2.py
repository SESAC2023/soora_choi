#정답
import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n, m, r = map(int, input().split())

graph = [ [] for i in range (n+1)]
visited = [False] * (n+1)
visitnum = [0] * (n+1)
num = 1

for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort(reverse=True)
#for i in graph 말고 이렇게 해야 리스트 하나씩 가져다가 정렬할듯
#sort(reverse=True) 이거 맞나??

def dfs(x):
  global num
  visited[x] = True
  visitnum[x] = num
  num+=1
  for i in graph[x]:
    if not visited[i]:
      dfs(i)

dfs(r)

for i in range(1,n+1):
  print(visitnum[i])



#오답 
  global num 누락
  
  Traceback (most recent call last):
  File "main.py", line 30, in <module>
    dfs(r)
  File "main.py", line 24, in dfs
    visitnum[x] = num
UnboundLocalError: local variable 'num' referenced before assignment
