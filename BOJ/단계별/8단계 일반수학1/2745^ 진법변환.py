#오답: a가 숫자일때가 고려X
import sys

A=[]
ans=0

a,b=sys.stdin.readline().split()

for i in a:
  A.append(ord(i)-55)

reversed_A=A[::-1]

for i in range (len(a)):
  ans+=reversed_A[i] * (int(b) ** i)
print(ans)


#진호님
data = input().split()
N = data[0]
B = int(data[1])

answer = 0
for i in range(len(N)):
    if N[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:  # 10진법을 넘지 않는 0-9는
        answer += int(N[i]) * (B**(len(N)-1-i))                     # 해당 숫자를 int로 type 변경 (10진법을 넘는 수가 있을 수 있으므로, 위에서 str로 입력 받았기 때문에)
    else:
        answer += (ord(N[i]) - 55) * (B**(len(N)-1-i))              # 10진법을 넘어가는 10-36진법은 A(10)-Z(35)로 표현하므로, 이를 반영할 수 있도록
                                                                    # 아스키코드를 이용
print(answer)

