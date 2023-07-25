#0이 N개 담긴 리스트 만들고 앞부터 약수 채워 넣고 마지막에 print(list[K]) 를 생각했으나 바꿔끼는게 더 어려울듯
#빈 리스트에 담고 리스트 넘어가면 0출력

N,K=map(int, input().split())
list=[]

for i in range(1,N+1):
  if N%i == 0:
    list.append(i)
if K <= len(list):
  print(list[K-1])
else:
  print(0)
