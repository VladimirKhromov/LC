class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = dict()
        for i, val in enumerate(nums):
            diff = target-val
            if diff in d:
                return [i, d[target-val]]
            d[val] = i