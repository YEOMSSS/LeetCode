# 삽입 정렬


Data = [2, 5, 3, 4, 1]

# 어차피 끝까지 확인해야 해서, howmany도 생략해버림
for i in range(1, len(Data)):
    key = Data[i]
    j = i - 1

    # key보다 큰 건 뒷방으로 넘기기
    # key가 가장 작은 경우, j가 -1이 되어 0번이 key가 된다.
    while key < Data[j] and j >= 0:
        Data[j + 1] = Data[j]
        j -= 1  # 거꾸로 올라간다.

    # key보다 작은 게 나오면 그 뒤 방에 key 내려놓기
    Data[j + 1] = key

print(Data)
