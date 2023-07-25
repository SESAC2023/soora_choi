#오답 - 답은 나오는데 런타임에

n=int(input())
list=list(map(int, input().split()))

for i in list:
  if i==1:
    list.remove(i)
  for j in range(2,i):
    if i%j == 0:
      #list에서 i 없애기
      list.remove(i)
print(len(list))


#다솔님
n = int(input())
num_list = list(map(int, input().split(" ")))

res = 0
for num in num_list:
  prime_num = True
  if num == 1:
    continue
  for i in range(2, num):
    if num % i == 0:
      prime_num = False
  if prime_num == True:
    res += 1
print(res)


#주영님
N = int(input())

num_list = list(map(int, input().split()))
count = 0

def prime_cheaker(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
            
for num in num_list:
    if prime_cheaker(num):
        count += 1

print(count)
