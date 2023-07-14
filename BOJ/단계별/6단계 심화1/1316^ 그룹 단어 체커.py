#드이어 정답 리턴 트루 오류.
n=int(input())
cnt=0

def group(data):
  visited = [False]*26
  for x in range(len(data)):
    if not visited[ord(data[x])-97]:
      visited[ord(data[x])-97] = True
    else:
      if data[x] != data[x-1]:
        return False
  return True

for i in range(n):
  data=input()
  if group(data):
    print('me')
    cnt+=1

print(cnt)      


# 답은 나오는데 오답- 마지막 예제에서 오답
n=int(input())
cnt=0

def group(data):
  visited = [False]*26
  for x in range(len(data)):
    if visited[ord(data[x])-97] == False:
      visited[ord(data[x])-97] = True
    else:
      if data[x] == data[x-1]:
        return True
      else:
        return False
  return True

for i in range(n):
  data=input()
  if group(data) == True:
    cnt+=1
print(cnt)      

#망함1
visited = [ False ] *26
data=input()

for i in range(len(data)):
  if visited[ord(data[i])-97] == False:
     visited[ord(data[i])-97] = True
  if data[i] == data[i-1]: #마지막값이 존재하지 않음
      continue
    
#망2
n=int(input())
cnt=0

visited = [False]*26

def group(data):
  for x in range(len(data)):
    if visited[ord(data[x])-97] == False:
      visited[ord(data[x])-97] = True
    else: #True였다면= 나온적있는 알파벳이라면: 직전 알파벳이 나랑 같은놈이여야 ㅇㅈ
      if data[x] == data[x-1]: #0에서는 무조건 false 일거라서 ㄱㅊ
        return True
      else:
        return False
      
for i in range(n):
  data=input()
  if group(data) == True:
    cnt+=1
print(cnt)      
      

  #한번나왔던 알파벳은 방문처리. 바로 다음꺼가 동일한 놈이면 트루인데, 멀리 떨어진애면 안돼
  #즉 조회해보니 트루인경우, 직전애랑 알파벳이 동일해야 그룹단어로 인정해ㅜㅁ
  
      



#멘토님👑
def group(string):
    # 각 알파벳에 대한 방문 여부
    chars = [False] * 26
    for i in range(len(string)):
        x = ord(string[i]) - 97
        # 방문한 적 없는 알파벳이라면
        if not chars[x]:
            chars[x] = True # 방문 처리
        # 방문한 적 있는 알파벳이라면
        else:
            # 직전 알파벳이랑 다르다면 그룹 단어 아님
            if string[i] != string[i - 1]:
                return False
    return True

n = int(input())
cnt = 0
for i in range(n):
    string = input()
    if group(string): cnt += 1
print(cnt)
