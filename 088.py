class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Initialize nums1's index
        i = m - 1
        # Initialize nums2's index
        j = n - 1
        # Initialize a variable k to store the last index of the 1st array...
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        return nums1



## TESTCASE 1 ##
s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
result = s.merge(nums1, m, nums2, n)
try:
    print(result)
    assert result == [1,2,2,3,5,6]
except AssertionError:
    print("TEST 1 Error")
else:
    print("TEST 1 ok")

## TESTCASE 2 ##
s = Solution()
nums1 = [1]
m = 1
nums2 = []
n = 0
result = s.merge(nums1, m, nums2, n)
try:
    print(result)
    assert result == [1]
except AssertionError:
    print("TEST 2 Error")
else:
    print("TEST 2 ok")