class Solution:
    def num_jewels_in_stones(self, jewels, stones):
        count = 0

        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    count += 1

        return count
