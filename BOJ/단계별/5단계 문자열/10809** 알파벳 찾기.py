#
word=input()
ans=[-1]*26
cnt=0

for i in word:
  x=ord(i)-97
  if ans[x]==-1:
    ans[x]=cnt
  cnt+=1

print(*ans)
    


#옛날
word = input()
l=len(word)
arr=[-1]*26

for i in range (l):
  for j in range (26):
      if ord(word[l-i-1]) == (97+j):
        arr[j]=l-i-1
        
for p in (arr):
  print(p, end=' ')

# for문에서 len,랑 26중에 누가 더 큰 범위 고민했었는데.. 똑같음 (근데 26을 바깥으로 뻈을때 시간이 더 짧게 나옴)
# ord(word[l-i]) 에서 오류난 원인 생각하는데 오래걸렸음
# 처음에는 별 생각없이 arr 0으로 깔았다가, 문득 -1로 디포트 깔아놓고 안 건드리면 되겠다 생각남
# 출력 때문에 또 틀림

#멘토님👑
"""
a부터 z까지의 아스키 코드 구하는 방법
print(ord("a")) a = 97
print(ord("b"))
print(ord("c"))
print(ord("d"))
print(ord("e"))
print(ord("f"))
print(ord("g"))
print(ord("z")) z = 122
"""

data = input()

characters = [-1] * 26
# characters[0]: a가 나온 위치
# characters[1]: b가 나온 위치
# ...
# characters[25]: z가 나온 위치

for i in range(len(data)):
    if characters[ord(data[i]) - 97] == -1:
        characters[ord(data[i]) - 97] = i

for x in characters:
    print(x, end=" ")

