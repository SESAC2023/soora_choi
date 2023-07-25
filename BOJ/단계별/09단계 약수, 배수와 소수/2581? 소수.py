#예제 답은 나오는데 '틀렸습니다.'

s=int(input())
b=int(input())
list=[]

for n in range(s, b+1): #60~100
  list.append(n)
  for i in range(2,n): #n은 소수인가?
    if n%i == 0:
      if n in list:
        list.remove(n)

if list:
  sum=0
  for i in list:
    sum+=i
  print(sum)
  print(list[0])
else:
  print(-1)


#주영님
M = int(input())
N = int(input())

def prime_cheaker(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum = 0
min = 0

for i in range(M, N+1):
    if prime_cheaker(i):
        sum += i
        if min == 0:
            min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)




#다솔님
m = int(input())
n = int(input())

prime_list = []
for num in range(m, n+1):
  prime_num = True  #해당 숫자의 소수 여부 저장 변수
  if num == 1:  #숫자가 1일 경우 스킵
    continue
  for i in range(2, num):  #숫자가 소수이면 list에 넣기
    if num % i == 0:
      prime_num = False
  if prime_num == True:
    prime_list.append(num)

if len(prime_list) == 0:
  print(-1)
else:
  print(sum(prime_list))
  print(min(prime_list))
