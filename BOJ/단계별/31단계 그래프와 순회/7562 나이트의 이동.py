#2 import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input=sys.stdin.readline

dx = [2, -2, 2, -2, 1, -1, 1 ,-1]
dy = [1, -1, -1, 1, 2, -2, -2, 2]

t_c=int(input())

for tc in range (t_c):
    n=int(input())
    s_x, s_y= map(int, input().split())
    e_x, e_y= map(int, input().split())

    visited = [ [False]*n for _ in range (n) ]
    distance = [ [-1]*n for _ in range (n) ]

    q=deque()
    q.append((s_x,s_y))
    visited[s_x][s_y] = True
    distance[s_x][s_y] = 0

    while q:
        x,y = q.popleft()
        if x==e_x and y==e_y:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if not visited[nx][ny]:
                visited[nx][ny]=True
                distance[nx][ny]= distance[x][y]+1
                q.append((nx,ny))

    print(distance[x][y])
#print에 distance[x],[y]라 쓴 것, dx dy 구분에 온점 섞여있던 것 때문에..


#1 의식의흐름 (실패메모)
import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

test_case=int(input())
for i in range (test_case):
    l=int(input())
    s_x, s_y=map(int, input().split())
    e_x, e_y=map(int, input().split())

'''
#최소 몇 번= 최단거리 :bfs
visited=[False]*(l**2)
while q:

cnt=0
def re():
  list=[(x+2, y+1),(x-2, y+1),(x+2, y-1),(x-2, y-1),(x+1, y+2),(x+1, y-2),(x-1, y+2),(x-1, y-2)]'''

#체스판-2차원배열-nxn 방문체크배열 만들기
#visited=[ [False*n] for_ in range (n) ] 아니고..
visited = [ [False] * n for _ in range(n) ]
#: vistied = [ [False],[False][False],[False],[False]...,[False]]

#체스판 각 위치까지의 "최단거리배열" 만들기
distance = [ [-1]*n for _ in range (n) ]

q = deque()
#q객체는 덱 사용할 것
#q에 넣었다 뺐다

#시작점부터 넣고, 주변으로 이동하면서 처음 도착할때 방문처리하고 횟수 증가시키기
q.append(s_x, s_y)
#?좌표로 넣. 튜플??
visited[s_x][s_y]=True
distace[s_x][s_y]=0
#시작점 설정완

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

#bfs 실행
#어떤 점에 있을 때, 8가지 이동경로에 가서 방문처리하고, distance +1, / 단 이미 갔던 곳은 무시 / 그 출발점은 pop
#!!언제까지? 도착지점에 e_x, e_y걸릴때까지. break
while q:
  #q.popleft() 아니고
  x,y = q.popleft()
  #종료 상황
  #if x,y=e_x, e_y 아니고
  if x == end_x and y == end_y:
    break
  #(dx, dy)=s_x+... 아니고
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    #체스판 빠져나가는거 조건설정
    if nx < 0 or nx > l,  :
      continue
  if not visited (nx, ny):
    visited[nx, ny] = True
    distance[nx, ny] +=1 #?
    q.append(nx, ny)



#멘토님
from collections import deque

#      0  1   2   3   4  5  6  7
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

test_cases = int(input())  # 테스트 케이스의 수
for tc in range(test_cases):
    n = int(input())  # 체스판의 길이
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    # N X N 크기의 체스판 방문 체크 배열 만들기
    visited = [[False] * n for _ in range(n)]
    # N X N 각 위치까지의 최단 거리 배열 만들기
    distance = [[-1] * n for _ in range(n)]

    # start 위치에서 BFS를 수행해서 최단 거리 계산
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True  # 방문 처리
    distance[start_x][start_y] = 0  # 시작 지점 거리

    # BFS 수행
    while q: # 큐가 빌 때까지 반복
        x, y = q.popleft()
        # 찾으면 break하도록 해서 시간 초과 방지
        if x == end_x and y == end_y:
            break
        for i in range(8): # 다음 위치(인접 위치) 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나는 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visited[nx][ny]: # 처음 방문한다면
                visited[nx][ny] = True # 방문 처리
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

    print(distance[end_x][end_y])
