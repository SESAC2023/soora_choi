data = input() #
data = data.split(" ") #문자열에 쓰는.. 쪼갠거 리스트로
data = list(map(int, data)) #문자열에 대해. data에 대해 int로 

a = data[0]
b = data[1]

print(a+b)
