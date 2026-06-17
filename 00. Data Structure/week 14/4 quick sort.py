def quich_sort(left, right):
    if left < right:
        pivot = partition(left, right)
        quich_sort(left, pivot - 1)
        quich_sort(pivot + 1, right)


def partition(left, right):
    where = left
    # 기준은 최좌측.
    princess = Data[where]

    while left < right:
        # 공주보다 left가 클 때까지 이동
        while left < len(Data) and Data[left] <= princess:
            left += 1
        # 공주보다 right가 작거나 같을 때까지 이동
        while Data[right] > princess:
            right -= 1
        # 둘 다 만족하면 서로 바꾸고 계속 진행한다.
        if left < right:
            Data[left], Data[right] = Data[right], Data[left]
    print(Data, where, princess, right, Data[right])

    # 엇갈리면 기준과 현재 right를 바꾼다.
    Data[where], Data[right] = Data[right], Data[where]
    # 현재 right를 기준으로 절반 나눈다.
    return right


Data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
quich_sort(0, len(Data) - 1)
print(Data)
