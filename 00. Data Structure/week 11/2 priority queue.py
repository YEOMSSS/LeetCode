pQueue = [None, 0, 2, 6, 3, 9, 8, 7, 5]

# 1을 삽입한다.
pQueue.append(1)
where = len(pQueue) - 1

# rshift로 부모와 비교하면서 부모가 더 작으면 바꾸며 올라간다.
while pQueue[where] < pQueue[where >> 1]:
    pQueue[where], pQueue[where >> 1] = pQueue[where >> 1], pQueue[where]
    where >>= 1  # where //= 2

print(pQueue)
