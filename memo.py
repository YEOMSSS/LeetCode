class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        real_sum = n * (n + 1) // 2
        error_sum = sum(nums)
        set_sum = sum(set(nums))
        return [error_sum - set_sum, real_sum - set_sum]
