class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0, 1):
            return x
        for i in range(x // 2 + 2):
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1






## TESTCASE 1 ##
s = Solution()
x = 3
result = s.mySqrt(x)
try:
    assert result == 1
except AssertionError:
    print("TEST 1 Error")
else:
    print("TEST 1 ok")

## TESTCASE 2 ##
s = Solution()
x = 8
result = s.mySqrt(x)
try:
    assert result == 2
except AssertionError:
    print("TEST 2 Error")
else:
    print("TEST 2 ok")

## TESTCASE 3 ##
s = Solution()
x = 5
result = s.mySqrt(x)
try:
    assert result == 2
except AssertionError:
    print("TEST 3 Error")
else:
    print("TEST 3 ok")
