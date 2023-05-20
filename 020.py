class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack


class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        brackets = ["()", "[]", "{}"]
        while True:
            for bracket in brackets:
                if bracket in s:
                    index = s.index(bracket)
                    s1 = s[:index]
                    s2 = s[index+2:] if index + 2 < len(s) else ""
                    s = s1 + s2
            if brackets[0] not in s and brackets[1] not in s and brackets[2] not in s:
                break
        if len(s) == 0:
            return True
        return False




s = Solution1()
res = s.isValid("(}")
print(res)

s = Solution2()
res = s.isValid("(}")
print(res)