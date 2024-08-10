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
