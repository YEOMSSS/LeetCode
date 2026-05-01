# 선택 정렬


def Selection_Sort(Data):
    howmany = len(Data)
    for now in range(howmany - 2):
        wheremin = now

        for fromhere in range(now + 1, howmany):
            if Data[fromhere] < Data[wheremin]:
                wheremin = fromhere
        Data[now], Data[wheremin] = Data[wheremin], Data[now]


Data = [3, 2, 5, 4, 1]
Selection_Sort(Data)
print(Data)
