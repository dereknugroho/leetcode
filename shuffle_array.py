class Solution:
    def shuffle(self, nums, n):
        if n == 0: return []

        shuffled_array = []
        i = 0
        j = n

        while i < n:
            shuffled_array.append(nums[i])
            shuffled_array.append(nums[j])
            i += 1
            j += 1

        return shuffled_array
