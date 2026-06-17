import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# --------------------

from collections import deque

Shalala, Zombie = map(int, input().split())
# ability = [0] * 3
# ability[0], ability[1], ability[2] = map(int, input().split())
ability = list(map(int, input().split()))


def bfs(start):
    queue = deque()
    # visited의 역할을 겸한다.
    Time = [sys.maxsize] * (Zombie + 1)

    queue.append(start)
    Time[start] = 0

    while queue:
        curr = queue.popleft()

        for ab in ability:
            nxt = curr + ab
            if nxt > Zombie:
                continue
            # 가지치기. 이미 Time[nxt]가 부모+1 보다 작거나 같다면 갱신할 필요가 없음
            # = 이미 방문했다면의 의미가 된다.
            if Time[nxt] <= Time[curr] + 1:
                continue
            Time[nxt] = Time[curr] + 1
            queue.append(nxt)

    if Time[Zombie] != sys.maxsize:
        print(Time[Zombie])


bfs(Shalala)
