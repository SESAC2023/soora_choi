total=[i+1 for i in range(30)]
for i in range(28):
  a=int(input())
  total.remove(a)

print(min(total[0],total[1]))
print(max(total[0],total[1]))
