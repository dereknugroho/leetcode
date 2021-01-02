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

sol = Solution()
nums1 = [2, 5, 1, 3, 4, 7]
n1 = 3
nums2 = [1, 2, 3, 4, 4, 3, 2, 1]
n2 = 4
nums3 = [1, 1, 2, 2]
n3 = 2

print('Input:    [2, 5, 1, 3, 4, 7], 3')
print('Output:  ', sol.shuffle(nums1, n1))
print('Expected: [2, 3, 5, 4, 1, 7]')
print('---')

print('Input:    [1, 2, 3, 4, 4, 3, 2, 1], 4')
print('Output:  ', sol.shuffle(nums2, n2))
print('Expected: [1, 4, 2, 3, 3, 2, 4, 1]')
print('---')

print('Input:    [1, 1, 2, 2], 2')
print('Output:  ', sol.shuffle(nums3, n3))
print('Expected: [1, 2, 1, 2]')
