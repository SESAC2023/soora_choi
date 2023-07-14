tc=int(input())
for i in range(tc):
    money=int(input())
    list=[]
    list.append(money//25)
    list.append(money%25//10)
    list.append(money%25%10//5)
    list.append(money%25%10%5)
    print(*list)
