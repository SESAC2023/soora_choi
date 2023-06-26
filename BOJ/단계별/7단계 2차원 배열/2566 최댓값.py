import sys
data=[]
m=[]

for i in range (9): #아홉줄을 입력 받는다 #data list에 한 줄을 하나의 list로 묶어서 넣는다: 2차원 배열
  data.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in data: #리스트로 묶여서 data litst에 들어가있는, 한 행씩 꺼내서 확인한다.
  m.append(max(i)) #각 행에서 최댓값을 찾아서 새로운 행렬m에 넣는다. : 각 행의 최댓값들을 요소로하는 리스트 m 생성완료

p1=m.index(max(m)) #리스트m 중 최댓값 = 전체 중 최댓값 #그 최댓값이 리스트m에서 몇번째 요소인지 확인하면 최댓값이 있는 행을 알 수 있다.:p1
p2=data[p1].index(max(m)) #그 행에서 그 최댓값이 몇번째 요소였는지 찾으면 열을 알 수 있다.: p2

print(max(m))
print(p1+1, p2+1)
