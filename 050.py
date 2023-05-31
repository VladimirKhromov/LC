class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res

    def myPow_2(self, x: float, n: int) -> float:
        return pow(x,n)

    def myPow_3(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = - n
        result = 1
        count = 0
        for _ in range(n):
            result = result * x

        return result


## TESTCASE 1 ##
s = Solution()
x = 2.000
n = 10
result = s.myPow(x,n)
try:
    print(result)
    assert result == 1024
except AssertionError:
    print("TEST 1 Error")
else:
    print("TEST 1 ok")


## TESTCASE 2 ##
s = Solution()
x = 2.10000
n = 3
result = s.myPow(x,n)
try:
    print(result)
    assert result == 9,26100
except AssertionError:
    print("TEST 2 Error")
else:
    print("TEST 2 ok")

## TESTCASE 3 ##
s = Solution()
x = 0.00001
n = 2147483647
result = s.myPow(x,n)
try:
    print(result)
    assert result == 9,26100
except AssertionError:
    print("TEST 3 Error")
else:
    print("TEST 3 ok")