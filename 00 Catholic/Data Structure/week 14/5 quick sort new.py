def quicksort(Data):
    if len(Data) <= 1:
        return Data
    pivot = Data[0]
    less, equal, greater = [], [], []

    for each in range(len(Data)):
        each = Data.pop()
        if each < pivot:
            less.append(each)
        elif each > pivot:
            greater.append(each)
        else:
            equal.append(each)
    print(less, equal, greater)

    return quicksort(less) + equal + quicksort(greater)


Data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(quicksort(Data))

# [2, 1, 4, 3] [5] [7, 6, 9, 8]
# [1] [2] [3, 4]
# [] [3] [4]
# [6] [7] [8, 9]
# [] [8] [9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
