import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\LeetCode\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-05-17
# Problem Number : 5177


# [Summary] 5177. [S/W 문제해결 기본] 8일차 - 이진 힙

# 이진 힙을 구현해서 마지막 노드의 조상 노드의 합을 출력하시오.


def main() -> None:

    # [Ideas]

    # 이진 힙을 구현해야 한다.
    # 부모보다 작으면 부모와 스왑하자.
    # 이후 마지막 노드 인덱스를 계속 rshift하며 누적하자.

    ##########

    T = int(input())

    for tc in range(1, T + 1):

        N = int(input())
        data = list(map(int, input().split()))

        # 인덱스 0을 채우고 시작
        min_heap = [0]

        for i, n in enumerate(data):
            # enum으로 뽑았으니까 1을 더해준다.
            i += 1

            min_heap.append(n)
            # 루트가 아닌 상태에서 부모보다 작은 경우 스왑
            while i > 1 and min_heap[i >> 1] > min_heap[i]:
                min_heap[i >> 1], min_heap[i] = min_heap[i], min_heap[i >> 1]
                i >>= 1

        # 조상을 타고 올라가며 누적
        result = 0
        while N > 1:
            N >>= 1
            result += min_heap[N]

        print(f"#{tc} {result}")

    ##########

    return


# [Review]

# 이진힙의 원리를 이해하자.


if __name__ == "__main__":
    main()
