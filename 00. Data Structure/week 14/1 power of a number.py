# 분할정복을 해보자. 반으로 일단 나누고 생각하자.


def GetSome(b):
    if b == 1:
        return a

    halfpower = GetSome(b // 2)
    if b & 1:  # 홀수인지 비트연산으로 확인하기
        return halfpower**2 * a
    else:
        return halfpower**2


a = 3
b = 4

print(GetSome(b))
