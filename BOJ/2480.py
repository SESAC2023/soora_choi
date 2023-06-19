a,b,c  =map(int, input().split())

if a==b:
  if b==c:
    print(10000+a*1000)
  if b!=c:
    print(1000+a*100)
if a!=b:
  if a==c or b==c:
    print(1000+c*100)
  if a!=c and b!=c:
    print(max(a,b,c)*100)
