class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''
        l = len(strs[0])

        for i in range(1, l+1):
            prefix = strs[0][:i]
            prefix_len = len(prefix)

            res = [(prefix in word[:prefix_len]) for word in strs]

            if all(res):
                result = prefix
            else:
                return result
                
        return result