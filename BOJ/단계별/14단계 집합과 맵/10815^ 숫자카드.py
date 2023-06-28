#시간초과
n=int(input())
card=list(map(int, input().split()))
m=int(input())
guess=list(map(int, input().split()))

ans = [0]*m
for i in range (m):
  if guess[i] in card:
    ans[i]=1

print(*ans)


#진우님
"""
이진탐색 -> 탐색범위가 매우 크게 주어지면 선형탐색으로는 시간초과
bisect -> 정렬된 리스트에서 특정 값을 매우 빠르게 찾고 싶을때 사용
시간 복잡도 O(logN)

정렬된 리스트에서 특정 값이 몇번 등장하는지 확인
-> a = bisect.bisect_left(card, i)
  b = bisect.bisect_right(card, i)
  b-a
"""

import sys
input = sys.stdin.readline
import bisect

N = int(input())
card = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

card.sort()
arr = [0] * M

for i in check:
    a = bisect.bisect_left(card, i)
    b = bisect.bisect_right(card, i)
    print(b-a, end=" ")
