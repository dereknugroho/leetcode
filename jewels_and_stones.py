class Solution:
    def num_jewels_in_stones(self, jewels, stones):
        count = 0

        # Assume no duplicates in jewels

        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    count += 1

        return count

# Test cases

sol = Solution()

jewels1 = 'aA'
stones1 = 'aAAbbbb'
expected1 = 3

jewels2 = 'z'
stones2 = 'ZZ'
expected2 = 0

print(f'Input:    \'{jewels1}\', \'{stones1}\'')
print(f'Output:   {sol.num_jewels_in_stones(jewels1, stones1)}')
print(f'Expected: {expected1}')
print('---')

print(f'Input:    \'{jewels2}\', \'{stones2}\'')
print(f'Output:   {sol.num_jewels_in_stones(jewels2, stones2)}')
print(f'Expected: {expected2}')
        