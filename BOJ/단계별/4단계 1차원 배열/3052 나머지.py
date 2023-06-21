arr=[]
for i in range(10):
  a=int(input())
  arr.append(a)

r=[i%42 for i in arr]
print(len(set(r)))
