import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
f=int(input())

print(arr.count(f))


#멘토님 2가지 솔루션 다른 하나는
cnt = 0
for i in range(n):
    if arr[i] == v:
        cnt += 1
print(cnt)
