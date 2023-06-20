import sys
while True:
  try:
    a,b=map(int, sys.stdin.readline().split())
    print(a+b)
  except:
    break



#시간초과 오답_braek를 pass로..:pass로 쓰면 다음 명령으로 넘어가서 시간초과
import sys
while True:
  try:
    a,b=map(int, sys.stdin.readline().split())
    print(a+b)
  except:
    pass
