class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #s = s.strip()
        return len(s.strip().split()[-1])



## TESTCASE ##
sol = Solution()
s = "   fly me   to   the moon  "
result = sol.lengthOfLastWord(s)
try:
    assert result == 4
except AssertionError:
    print("TEST Error")
else:
    print("TEST ok")
