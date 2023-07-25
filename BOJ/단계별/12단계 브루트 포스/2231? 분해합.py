#오답

n=int(input())
list=[]
sumi=0

for i in range(n): # i: 생성자
  # 생성자의 각자리 수의 합 sumi 구하기
  i=str(i)
  for j in range(len(i)):
    sumi += int(i[j])
  # 자연수 == 생성자 + sumi 이면 리스트에 추가
  if n-int(i) == sumi:
    list.append(i)
    
print(list) #list에 생성자 담아서 그 중 최소값 출력하려했는데 엉뚱한 숫자 나옴



#다솔님
n = int(input())

# 숫자가 들어왔을 때 생성자를 return하는 함수
def check(x):
  res = x
  x_str = str(x)
  for i in range(len(x_str)):
    res += int(x_str[i])
  return res

# 처음으로 등장하는(가장 작은) 생성자 출력
for i in range(n):
  if check(i) == n:
    print(i)
    break
else: print(0)


