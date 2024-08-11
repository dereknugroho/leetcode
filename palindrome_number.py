class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        x = str(x)
        i = 0
        while i <= len(x) / 2:
            if x[i] != x[-1 - i]:
                return False
            i += 1
        return True
