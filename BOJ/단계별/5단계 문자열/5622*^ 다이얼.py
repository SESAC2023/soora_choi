#정답
word=input()
time=0

for i in word:
  if i in ['A', 'B', 'C']:
    time+=3
  elif i in ['D', 'E', 'F']:
    time+=4    
  elif i in ['G', 'H', 'I']:
    time+=5
  elif i in ['J', 'K', 'L']:
    time+=6
  elif i in ['M', 'N', 'O']:
    time+=7
  elif i in ['P', 'Q', 'R', 'S']:
    time+=8
  elif i in ['T', 'U', 'V']:
    time+=9
  elif i in ['W', 'X', 'Y', 'Z']:
    time+=10

print(time)


#진호님
data = input()

temp = []
for j in data:
    if j in ['A', 'B', 'C']:
        temp.append(3)
    elif j in ['D', 'E', 'F']:
        temp.append(4)
    elif j in ['G', 'H', 'I']:
        temp.append(5)
    elif j in ['J', 'K', 'L']:
        temp.append(6)
    elif j in ['M', 'N', 'O']:
        temp.append(7)
    elif j in ['P', 'Q', 'R', 'S']:
        temp.append(8)
    elif j in ['T', 'U', 'V']:
        temp.append(9)
    elif j in ['W', 'X', 'Y', 'Z']:
        temp.append(10)

print(sum(temp))


#주영님
alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for unit in alpabet_list :  
    for i in unit:       # alpabet 리스트 각 요소를 한글자씩 분리
        for x in word :  # 입력받은 문자를 하나씩 분리
            if i == x :  # 두 알파벳이 같으면
                time += alpabet_list.index(unit) +3
print(time)


#다솔님
word = input()

tel_dict = {'ABC': 2, 'DEF':3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ' : 9}

t = 0
for letter in word:
  for key, value in tel_dict.items():
    if letter in key:
      num = tel_dict[key]
  t += (num+1)

print(t)
