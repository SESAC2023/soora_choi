sum=0
num=0
for i in range(20):
  a,b,c=input().split()
  if c != 'P': #P/F 시험은 계산에 포함하지 않기 때문에 이 경우가 아닌 경우만 계산진행
    if c=='A+':
      intc=4.5
    elif c=='A0':
      intc=4.0
    elif c=='B+':
      intc=3.5
    elif c=='B0':
      intc=3.0
    elif c=='C+':
      intc=2.5
    elif c=='C0':
      intc=2.0
    elif c=='D+':
      intc=1.5
    elif c=='D0':
      intc=1.0
    elif c=='F':
      intc=0
    num+=float(b)
    sum+=float(b)*intc

print(sum/num)
