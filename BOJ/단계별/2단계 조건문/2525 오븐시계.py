a,b=map(int, input().split())
c=int(input())

num=0

while c>60: #c분에 몇시간 들어가는지 개수 세면서, 변수c에 분만 남기기
  c=c-60
  num=num+1

if c<=60:
  if b+c<60:
    if a+num>=24:
      print(a+num-24, b+c)
    else:
      print(a+num, b+c)
  else:
    if a+num>=23:
      print(a+num-23, b+c-60)
    else:
      print(a+num+1, b+c-60)

#c<=60에도 while로 잘못썼다가 무한루프
#c<=60내에서 기준점 정할때 a+num로 했다가 fail
