#뒤집어주는 a,b를 기준으로 나눠서 처리하고 하나의 리스트로 다시 합치려고 생각하다가 실패
#셈을 1부터 하는 경우, 그 변수에 1 빼주고 들어가기 (a -= 1)
#멘토님 방법2??


#정답😑
n,m=map(int, input().split())
list=[i+1 for i in range(n)]
for i in range(m):
    a,b=map(int, input().split())
    list[a-1:b]=reversed(list[a-1:b])
    
print(*list)


#멘토님👑1
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    arr[a:b] = reversed(arr[a:b])

for x in arr:
    print(x, end=" ")


#멘토님👑2 ????
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for i in range(m):
    left, right = map(int, input().split())
    left -= 1
    temp = []
    for j in range(left, right):
        temp.append(arr[j])
    for j in range(left, right):
        arr[j] = temp.pop()

for x in arr:
    print(x, end=" ")
