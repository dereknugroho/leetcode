class Solution:
    def maximum_wealth(self, accounts):
        max_wealth = 0

        for customer in accounts:
            customer_wealth = 0
            for bank in customer:
                customer_wealth += bank
            if customer_wealth >= max_wealth:
                max_wealth = customer_wealth
                
        return max_wealth

# Test cases

sol = Solution()

accounts1 = [[1, 2, 3], [3, 2, 1]]
expected1 = 6

accounts2 = [[1, 5], [7, 3], [3, 5]]
expected2 = 10

accounts3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
expected3 = 17

print(f'Input:    {accounts1}')
print(f'Output:   {sol.maximum_wealth(accounts1)}')
print(f'Expected: {expected1}')
print('---')

print(f'Input:    {accounts2}')
print(f'Output:   {sol.maximum_wealth(accounts2)}')
print(f'Expected: {expected2}')
print('---')

print(f'Input:    {accounts3}')
print(f'Output:   {sol.maximum_wealth(accounts3)}')
print(f'Expected: {expected3}')
