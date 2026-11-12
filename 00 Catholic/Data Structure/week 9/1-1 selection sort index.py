# 선택 정렬, .index를 사용하는 경우.
# 시간에는 차이가 없다.


def Selection_Sort(Data: list):
    howmany = len(Data)
    for now in range(howmany - 2):
        # 그냥 코드가 몇 줄 짧아진 정도다. 간결해보여서 좋긴 하다.
        wheremin = Data.index(min(Data[now:howmany]))
        Data[now], Data[wheremin] = Data[wheremin], Data[now]


Data = [3, 2, 5, 4, 1]
Selection_Sort(Data)
print(Data)
