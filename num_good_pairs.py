class Solution:
    def num_identical_pairs(self, nums):
        pair_count = 0
        i = 0

        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    pair_count += 1
                j += 1
            i += 1

        return pair_count
