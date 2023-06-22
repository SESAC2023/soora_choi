#희묵님
n, k = map(int, input().split())

count = 0
for h in range(0, n + 1):
  for m in range(0, 60):
    for s in range(0, 60):
      if (h // 10 == k) or (h % 10 == k):
        count += 1
      elif (m // 10 == k) or (m % 10 == k):
        count += 1
      elif (s // 10 == k) or (s % 10 == k):
        count += 1
        
print(count)



#멘토님
n, k = map(int, input().split())

cnt = 0
for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            hour = str(hour).zfill(2)
            minute = str(minute).zfill(2)
            second = str(second).zfill(2)
            current = hour + minute + second
            if str(k) in current:
                cnt += 1

print(cnt)

#zfill(2) 두자리 안되면 빈자리 0 넣
