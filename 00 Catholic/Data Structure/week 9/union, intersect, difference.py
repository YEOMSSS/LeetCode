def union(listA, listB):
    listC = []
    i = 0
    j = 0
    sizeA = len(listA)
    sizeB = len(listB)

    while i < sizeA and j < sizeB:
        a = listA[i]
        b = listB[j]
        if a == b:
            listC.append(a)
            i += 1
            j += 1
        elif a < b:
            listC.append(a)
            i += 1
        else:
            listC.append(b)
            j += 1

    while i < sizeA:
        listC.append(listA[i])
        i += 1

    while j < sizeB:
        listC.append(listB[j])
        j += 1

    return listC


def intersect(listA, listB):
    listC = []
    i = 0
    j = 0
    sizeA = len(listA)
    sizeB = len(listB)

    while i < sizeA and j < sizeB:
        a = listA[i]
        b = listB[j]
        if a == b:
            listC.append(a)
            i += 1
            j += 1
        elif a < b:
            i += 1
        else:
            j += 1

    return listC


def difference(listA, listB):
    listC = []
    i = 0
    j = 0
    sizeA = len(listA)
    sizeB = len(listB)

    while i < sizeA and j < sizeB:
        a = listA[i]
        b = listB[j]
        if a == b:
            i += 1
            j += 1
        elif a < b:
            listC.append(a)
            i += 1
        else:
            j += 1

    while i < sizeA:
        listC.append(listA[i])
        i += 1

    return listC


A = [1, 3, 5, 7]
B = [2, 3, 6, 7, 9]

print(union(A, B))
print(intersect(A, B))
print(difference(A, B))
