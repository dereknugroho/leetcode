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
