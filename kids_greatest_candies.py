class Solution:
    def kids_with_candies(self, candies, extra_candies):
        can_have_greatest = []
        max_candies = 0

        for kid_candies in candies:
            if kid_candies > max_candies:
                max_candies = kid_candies

        for kid_candies in candies:
            kid_maximum = kid_candies + extra_candies
            can_have_greatest.append(kid_maximum >= max_candies)

        return can_have_greatest

sol = Solution()
candies1 = [2,3,5,1,3]
extra1 = 3
candies2 = [4,2,1,1,2]
extra2 = 1
candies3 = [12,1,12]
extra3 = 10

print('Input:    [2,3,5,1,3], 3')
print('Output:  ', sol.kids_with_candies(candies1, extra1))
print('Expected: [True, True, True, False, True]')
print('---')

print('Input:    [4,2,1,1,2], 1')
print('Output:  ', sol.kids_with_candies(candies2, extra2))
print('Expected: [True, False, False, False, False]')
print('---')

print('Input:    [12,1,12], 10')
print('Output:  ', sol.kids_with_candies(candies3, extra3))
print('Expected: [True, False, True]')
