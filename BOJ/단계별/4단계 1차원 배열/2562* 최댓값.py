#한줄씩 입력받아서 리스트에 넣고
#max=0 랑 비교해서 더 큰 값 저장
#마지막 max의 위치찾기
max = 0
list=[]

for i in range(9):
  a=int(input())
  list.append(a)
  if a > max :
    max = a
print(max)
print(list.index(max)+1)


#i=i+1로 (인덱스 대신) 잘못접근
