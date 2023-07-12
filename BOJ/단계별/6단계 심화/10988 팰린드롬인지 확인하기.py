#1,2: 앞뒤 문자 같은지 확인
#3,4: 뒤집어서 기존값이랑 동일한지 확인
#팰린드롬 함수
#reversed(data) 혹은 data[::-1]로 뒤집을 수 있다는 것 


#1. 문자열 앞뒤 동일한지 확인하기
data=input()
n=len(data)//2

for i in range(n):
    if data[i] == data[-i-1]:
        n -= 1

if n == 0:
    print(1)
else:
    print(0)


#2/ 멘토님👑1
#팰린드롬 함수_ 마지막 문자의 번호를 전체길이-i-1로 해서 i번째랑 비교
def pelindrome(data):
    for i in range(len(data)):
        if data[i] != data[len(data) - i - 1]:
            return False
    return True

data = input()

if pelindrome(data):
    print(1)
else:
    print(0)


#3. 멘토님👑2
#뒤집은걸 새변수에 저장하고, 기존이랑 동일한지 확인
data = input()
reversed_data = reversed(data)

if data == reversed_data:
    print(1)
else:
    print(0)



#4. 멘토님👑3
#revered(data) 말고, data[::-1]로 뒤집어서 저장
data = input()
reversed_data = data[::-1] # 이 코드는 많이 쓰임
# data[2:5] == [data[2], data[3], data[4]]
# data[2:5:-1] == [data[4], data[3], data[2]]
# data[:] == data
# data[::-1] == reversed(data)
# (start, end, step)

if data == reversed_data:
    print(1)
else:
    print(0)
