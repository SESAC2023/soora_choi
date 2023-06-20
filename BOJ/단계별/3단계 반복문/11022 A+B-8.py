#1
t=int(input())

for i in range(t):
  a,b=map(int, input().split())
  print("Case #" + str(i+1) + ": " + str(a) + " + " + str(b) + " = " + str(a+b) )

#2 f-string
t=int(input())

for i in range(t):
  a,b=map(int, input().split())
  print(f"Case #{i+1}: {a} + {b} = {a+b}")


#입력을 for문 안에서 받야야지, 아까처럼 for문 밖에서 ()들어오면 변수에 그 값 입력된 상태로 for문에서 돌아서 같은 값만 t번 출력
# i+1 대신 t 넣지마..
