class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits == [9]:
            return [1, 0]
        elif digits[-1] != 9:
            digits[-1] += 1
            return digits
        elif digits[-1] == 9:
            return self.plusOne(digits[:-1]) + [0] 



## TESTCASE 1 ##
s = Solution()
digits = [1,2,3]
result = s.plusOne(digits)
try:
    assert result == [1,2,4]
except AssertionError:
    print("TEST 1 Error")
else:
    print("TEST 1 ok")

## TESTCASE 2 ##
s = Solution()
digits = [9]
result = s.plusOne(digits)
try:
    assert result == [1,0]
except AssertionError:
    print("TEST 2 Error")
else:
    print("TEST 2 ok")

## TESTCASE 3 ##
s = Solution()
digits = [9, 9]
result = s.plusOne(digits)
try:
    assert result == [1,0,0]
except AssertionError:
    print("TEST 3 Error")
else:
    print("TEST 3 ok")
