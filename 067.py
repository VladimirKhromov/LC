class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a,2) + int(b,2))[2:])



## TESTCASE 1 ##
s = Solution()
a = "11"
b = "1"
result = s.addBinary(a,b)
try:
    assert result == "100"
except AssertionError:
    print("TEST 1 Error")
else:
    print("TEST 1 ok")

## TESTCASE 2 ##
s = Solution()
a = "1010"
b = "1011"
result = s.addBinary(a,b)
try:
    assert result == "10101"
except AssertionError:
    print("TEST 2 Error")
else:
    print("TEST 2 ok")
