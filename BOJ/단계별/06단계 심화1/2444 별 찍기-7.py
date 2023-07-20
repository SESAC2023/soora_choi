x=int(input())
for i in range(x): #0~4
  print(' '*(x-1-i) + '*'*(2*i+1))
for i in range(x-1): #0~3
    print(' '*(i+1) + '*'*(2*x-3-2*i))

#진우님
x = int(input())
for i in range(1, x):
    print(" " * (x-i) + "*" * (2*i-1))
for j in range(x, 0, -1): # x부터 1까지 감소하는 for문
    print(" " * (x-j) + "*" * (2*j-1))
