word = input()
l=len(word)
arr=[-1]*26

for i in range (l):
  for j in range (26):
      if ord(word[l-i-1]) == (97+j):
        arr[j]=l-i-1
        
for p in (arr):
  print(p, end=' ')


