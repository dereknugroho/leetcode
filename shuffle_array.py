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

# Test cases

sol = Solution()

nums1 = [2, 5, 1, 3, 4, 7]
n1 = 3
expected1 = [2, 3, 5, 4, 1, 7]

nums2 = [1, 2, 3, 4, 4, 3, 2, 1]
n2 = 4
expected2 = [1, 4, 2, 3, 3, 2, 4, 1]

nums3 = [1, 1, 2, 2]
n3 = 2
expected3 = [1, 2, 1, 2]

print(f'Input:    {nums1}, {n1}')
print(f'Output:   {sol.shuffle(nums1, n1)}')
print(f'Expected: {expected1}')
print('---')

print(f'Input:    {nums2}, {n2}')
print(f'Output:   {sol.shuffle(nums2, n2)}')
print(f'Expected: {expected2}')
print('---')

print(f'Input:    {nums3}, {n3}')
print(f'Output:   {sol.shuffle(nums3, n3)}')
print(f'Expected: {expected3}')
