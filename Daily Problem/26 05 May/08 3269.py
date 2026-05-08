# -------------------------------
# Link : https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/description/?envType=daily-question&envId=2026-05-08
# -------------------------------

# Authored by : marigold2003
# Date : 2026-05-08
# Problem Number : 3629

# -------------------------------

# [Problem] Minimum Jumps to Reach End via Prime Teleportation

# 1M까지의 자연수로 이루어진 100K보다 크기가 같거나 작은 배열 nums가 들어온다.
# 좌우로 이동이 가능하며, 소수인 칸에서는 자신으로 나눠지는 값을 가진 칸으로 이동이 가능하다.
# 인덱스 0에서 인덱스 -1까지 가는 이동 횟수의 최솟값을 구하시오.


# [Intuition]

# 포탈이 열리는 걸 생각해보면, 이건 그래프이다. bfs로 최단경로를 찾는 것이다.
# 그렇다면 소수에서 어디로 포탈을 탈 수 있는지를 구해야한다.
# 각 수를 다 나눠보는 건 불가능하다. 각 수가 어떤 소수를 약수로 갖는지를 저장해두는 편이 좋겠다.
# 딕셔너리에 소수 : 그 소수로 나눠지는 값을 가진 인덱스의 배열, 로 저장하자.
# 그러면 소수인 칸에 도달할 때 bfs nei로 그 인덱스를 그대로 쓰면 되겠다.

# [Approach]

# 1. 1M까지의 소수 판정 표와 소인수 표를 동시에 구한다.
# 2. nums에 있는 소수들을 배수로 가지는 인덱스를 defaultdict로 저장한다.
# 3. bfs를 이용해 최단거리를 구한다. nei는 앞뒤와 소수인 경우 defaultdict가 포함된다.
# 4. bfs 과정에서 텔레포트를 사용한 소수 값을 이용해 다시 텔레포트할 필요가 없다. clear로 날린다.


# -------------------------------


def sieve(n):
    prime_factors = [[] for _ in range(n + 1)]
    is_prime = [True] * (n + 1)

    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            prime_factors[i].append(i)
            for multiple in range(i * 2, n + 1, i):
                is_prime[multiple] = False
                prime_factors[multiple].append(i)

    return is_prime, prime_factors


from collections import defaultdict, deque


def solve(nums: list[int]) -> int:

    ##########

    N = len(nums)

    if N == 1:
        return 0

    is_prime, prime_factors = sieve(max(nums))

    prime_to_idx = defaultdict(list)
    for i, n in enumerate(nums):
        for p in prime_factors[n]:
            prime_to_idx[p].append(i)

    # print(prime_to_idx)
    # print(prime_factors)

    # bfs
    queue = deque()
    visited = [False] * N

    queue.append(0)
    visited[0] = True

    result = 0
    while queue:
        result += 1

        for _ in range(len(queue)):
            curr = queue.popleft()

            if curr == N - 1:
                return result - 1

            if is_prime[nums[curr]]:

                for pi in prime_to_idx[nums[curr]]:
                    if visited[pi]:
                        continue
                    visited[pi] = True
                    queue.append(pi)

                prime_to_idx[nums[curr]].clear()

            if curr - 1 >= 0 and not visited[curr - 1]:
                visited[curr - 1] = True
                queue.append(curr - 1)
            if curr + 1 < N and not visited[curr + 1]:
                visited[curr + 1] = True
                queue.append(curr + 1)

    ##########

    return -1


# -------------------------------
# [LeetCode]
# -------------------------------


class Solution:
    def minJumps(self, nums: list[int]) -> int:

        return solve(nums)


# -------------------------------

# [Summary]

# 응, 시간초과야~ 다시 할 수 있도록.
# 소인수를 구하는 체로 다시 만들고, 사용한 소수는 재사용할 필요가 없다.


# [Review]

# 난이도 진짜 들쭉날쭉하네
# 이게 같은 medium이라고
# 좆 같네...

# -------------------------------
# -------------------------------


import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # [Input]

    nums = list(map(int, input().split()))

    print(solve(nums))
