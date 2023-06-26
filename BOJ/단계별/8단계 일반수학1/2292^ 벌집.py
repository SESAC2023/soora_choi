#1:1  1개
#2:2~7  6개 6*1
#3:8~19  12개 6*2
#4 20~37 18개 6*3
#n 6*(n-1)



#진우님
N = int(input())

bulzip = 1
total_cnt = 1

while N > bulzip:
    bulzip += 6 * total_cnt
    total_cnt += 1
print(total_cnt)


#다솔님
n = int(input())

num = 1
idx = 1
while n > num:
  num = num + (6*idx)
  idx += 1

print(idx)
