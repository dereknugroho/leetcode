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
accounts2 = [[1, 5], [7, 3], [3, 5]]
accounts3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]

print('Input:    [[1, 2, 3], [3, 2, 1]]')
print('Output:  ', sol.maximum_wealth(accounts1))
print('Expected: 6')
print('---')

print('Input:    [[1, 5], [7, 3], [3, 5]]')
print('Output:  ', sol.maximum_wealth(accounts2))
print('Expected: 10')
print('---')

print('Input:    [[2, 8, 7], [7, 1, 3], [1, 9, 5]]')
print('Output:  ', sol.maximum_wealth(accounts3))
print('Expected: 17')
