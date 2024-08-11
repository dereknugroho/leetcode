class Solution(object):
    def romanToInt(self, s):
        num, i = 0, 0
        while i < len(s):
            if s[i] == 'I':
                if i + 1 < len(s) and s[i + 1] in ('V', 'X'):
                    num -= 1
                else:
                    num += 1
            elif s[i] == 'V':
                num += 5
            elif s[i] == 'X':
                if i + 1 < len(s) and s[i + 1] in ('L', 'C'):
                    num -= 10
                else:
                    num += 10
            elif s[i] == 'L':
                num += 50
            elif s[i] == 'C':
                if i + 1 < len(s) and s[i + 1] in ('D', 'M'):
                    num -= 100
                else:
                    num += 100
            elif s[i] == 'D':
                num += 500
            elif s[i] == 'M':
                num += 1000
            i += 1
        return num
