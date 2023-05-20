class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900,
            }
        l = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']
        result = 0
        i = 0
        lens = len(s)
        while i < lens:
            if i+1 < lens and s[i:i+2] in l:
                result += d[s[i:i+2]]
                i += 2
            else:
                result += d[s[i]]
                i += 1
        return result