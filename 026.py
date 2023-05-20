class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
res = s.removeDuplicates(nums)
print(res)

