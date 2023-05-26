class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        index_start = 0
        index_end = len(nums)-1
        while index_start <= index_end:
            index_mid = (index_end + index_start) // 2
            if nums[index_mid] == target:
                return index_mid
            elif nums[index_mid] > target:
                index_end = index_mid - 1
            elif nums[index_mid] < target:
                index_start = index_mid + 1
        return index_end + 1




s = Solution()
nums = [1,3,5,6]
target = 5
result = s.searchInsert(nums, target)
print(result)


s = Solution()
nums = [1,3,5,6]
target = 2
result = s.searchInsert(nums, target)
print(result)

s = Solution()
nums = [1,3,5,6]
target = 7
result = s.searchInsert(nums, target)
print(result)
