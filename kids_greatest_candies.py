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

# Test cases

sol = Solution()

candies1 = [2, 3, 5, 1, 3]
extra1 = 3
expected1 = [True, True, True, False, True]

candies2 = [4, 2, 1, 1, 2]
extra2 = 1
expected2 = [True, False, False, False, False]

candies3 = [12, 1, 12]
extra3 = 10
expected3 = [True, False, True]

print(f'Input:    {candies1}, {extra1}')
print(f'Output:   {sol.kids_with_candies(candies1, extra1)}')
print(f'Expected: {expected1}')
print('---')

print(f'Input:    {candies2}, {extra2}')
print(f'Output:   {sol.kids_with_candies(candies2, extra2)}')
print(f'Expected: {expected2}')
print('---')

print(f'Input:    {candies3}, {extra3}')
print(f'Output:   {sol.kids_with_candies(candies3, extra3)}')
print(f'Expected: {expected3}')
