#f문자열 중앙 정렬
n=int(input())

for i in range(n):
  print(f'{"*"*(2*i+1):^{(2*n-1)}}')

for i in range(n-2, -1, -1):
    print(f'{"*" * (2 * i + 1):^{(2 * n - 1)}}')


#진호님
N = int(input())

for i in range(1, 2*N):
    if i>(2*N)//2:        # 주어지는 숫자 N에 따라 2*N의 반절이 넘어가면서 부터는 별의 갯수가 줄어들어야 한다.
        print(' '*(i-N) + ((2*N-i)*2-1)*'*')
    else:
        print(' '*(N-i) + (2*i-1)*'*')

#희묵님
  n = int(input())
for i in range(1, n+1):
    line = ' '*(n-i) + '*'*(2*i-1)
    print(line)
    
for j in range(n-1, 0, -1):
    line = ' '*(n-j) + '*'*(2*j-1)
    print(line)

#진우님
x = int(input())
for i in range(1, x):
    print(" " * (x-i) + "*" * (2*i-1))
for j in range(x, 0, -1): # x부터 1까지 감소하는 for문
    print(" " * (x-j) + "*" * (2*j-1))
