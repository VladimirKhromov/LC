class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

s = Solution()
nums = [0,1,2,2,2,2,3,0,4,2]
res = s.removeElement(nums, 2)
print(res)

