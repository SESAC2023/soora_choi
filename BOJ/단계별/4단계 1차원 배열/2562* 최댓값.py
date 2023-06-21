M=0
arr=[]
for i in range (9):
  a=int(input())
  arr.append(a)
  if M<a:
    M=a
    i=i+1
print(M)
print(arr.index(M)+1)

#i+1로 잘못접근
