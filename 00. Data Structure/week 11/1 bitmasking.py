a = 3
b = 5

# 음수로 변환하는 방법
print(~a + 1)

# 홀수이지 판별하는 방법
if a % 2 == 1:
    print("홀수")
if a & 1:  #  홀수는 마지막 비트가 1이니까. 1이랑 &연산하면 1이 된다.
    print("홀수")

# shift 연산은 사칙연산보다 속도가 훨씬 빠르다.
# left shift 한번. *2
print(a << 1)
# left shift 세번. *2*2*2
print(a << 3)

# 중간값 구하기 rshift. (A+B)//2
print((a + b) >> 1)
