Data = [2, 3, 4, 1, 5]


for i in range(1, len(Data)):
    bChanged = False

    for j in range(len(Data) - i):
        if Data[j] > Data[j + 1]:
            Data[j], Data[j + 1] = Data[j + 1], Data[j]
            bChanged = True

    if not bChanged:  # not이 있어야 한다.
        break

print(Data)
