#아이디어1 while X//b >= b: 더 나눌 수 없을 때, 그 몫을 리스트에 담는다. 순서대로 출력하면 답
#아이디어2 몇제곱까지인지 확인하고 동전거스름돈처럼 큰단위부터 분배
﻿n,b = map(int,input().split())
w = ""
while n != 0 :
  a = n % b
  if a >= 10:
    w += chr(a+55)
  else:
    w += str(a)
  n //= b
    
print(w[::-1])

﻿
#아이디어1이랑 반대 - b로 나눠서 자잘한 값부터 작은단위로 처리. 거꾸로 출력
#진우님
n,b = map(int,input().split())
ans = ""
while n!=0:
    a = n % b
    if a >= 10:
        ans += chr(a+55)
    else:
        ans += str(a)
    n //= b
print(ans[::-1])


#주영님
import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))

count = []
temp = N

while(1):
    if temp < M:
        count.append(temp)
        break
    count.append(temp % M)
    temp = temp //M

for i in reversed(range(len(count))):
    if count[i] < 10:
        print(count[i], end = '')
    else:
        print(chr(count[i]+55), end= '')
