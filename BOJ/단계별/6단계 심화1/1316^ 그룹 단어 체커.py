#망함
visited = [ False ] *26
data=input()

for i in range(len(data)):
  if visited[ord(data[i])-97] == False:
     visited[ord(data[i])-97] = True
  if data[i] == data[i-1]: #마지막값이 존재하지 않음
      continue
    

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
