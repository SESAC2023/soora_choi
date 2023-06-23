#문자열상태로
a,b=input().split()

anew=int(a[2]+a[1]+a[0])
bnew=int(b[2]+b[1]+b[0])

if anew>bnew:
  print(anew)
else:
  print(bnew)

#세 자리수라 그래서 직접 뒤집
#처음에 리스트에 넣고 했는데 문자열 상태로
a,b=input().split()
alist=[]
blist=[]
for i in a:
  alist.append(i)
for i in b:
  blist.append(i)

anew=int(alist[2]+alist[1]+alist[0])
bnew=int(blist[2]+blist[1]+blist[0])

if anew>bnew:
  print(anew)
else:
  print(bnew)


#진호님
import sys

a, b = sys.stdin.readline().rstrip().split()

a = a[::-1]
b = b[::-1]

if a > b:
    print(a)
elif a < b:
    print(b)
