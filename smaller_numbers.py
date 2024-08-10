class Solution:
    def smaller_numbers_than_current(self, nums):
        i = 0
        j = 0
        counts = []

        while i < len(nums):
            count = 0
            j = 0
            
            while j < len(nums):
                if i != j:
                    if nums[i] > nums[j]:
                        count += 1
                j += 1
            
            counts.append(count)
            i += 1

        return counts
