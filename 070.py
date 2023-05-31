class Solution:
    cache = {0: 0, 1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:

        if n in Solution.cache:
            return Solution.cache[n]
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        Solution.cache[n] = result
        print(Solution.cache)
        return result



## TESTCASE 1 ##
s = Solution()
x = 2
result = s.climbStairs(x)
try:
    print(result)
    assert result == 2
except AssertionError:
    print("TEST 1 Error")
else:
    print("TEST 1 ok")

## TESTCASE 2 ##
s = Solution()
x = 40
result = s.climbStairs(x)
try:
    print(result)
    assert result == 3
except AssertionError:
    print("TEST 2 Error")
else:
    print("TEST 2 ok")