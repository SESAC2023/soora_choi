#정답
while True:
    try:
        data=input()
        print(data)
    except:
        break

#오답
while True:
    try:
        data=input().readline() #readline 없어야 해
        print(data)
    except:
        break

#진호님
while True:
    try:
        print(input())
    except EOFError:    # EOF: End Of File. 즉 입력값이 더 이상 없는 상황을 뜻함 => 그런데 이때 EOFError를 사용하기 위해서는 sys.stdin.readline()을 사용해서는 안됨. input()을 사용해야 함.
        break           # 입력값이 더 이상 없으면 멈춰라.

#주영님
while(1):
  try: print(input())
  except: break


#은선님
import sys
input = sys.stdin.readline


for i in range(100) :
    a=input()
    print(a.strip()) #공백 삭제를 안 해서 계속 오류 났었음.
