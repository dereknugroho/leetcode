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

# Test cases

sol = Solution()

nums1 = [1, 2, 3, 1, 1, 3]
expected1 = 4

nums2 = [1, 1, 1, 1]
expected2 = 6

nums3 = [1, 2, 3]
expected3 = 0

print(f'Input:    {nums1}')
print(f'Output:   {sol.num_identical_pairs(nums1)}')
print(f'Expected: {expected1}')
print('---')

print(f'Input:    {nums2}')
print(f'Output:   {sol.num_identical_pairs(nums2)}')
print(f'Expected: {expected2}')
print('---')

print(f'Input:    {nums3}')
print(f'Output:   {sol.num_identical_pairs(nums3)}')
print(f'Expected: {expected3}')