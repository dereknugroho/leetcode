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

# Test cases

sol = Solution()

nums1 = [8, 1, 2, 2, 3]
expected1 = [4, 0, 1, 1, 3]

nums2 = [6, 5, 4, 8]
expected2 = [2, 1, 0, 3]

nums3 = [7, 7, 7, 7]
expected3 = [0, 0, 0, 0]

print(f'Input:    {nums1}')
print(f'Output:   {sol.smaller_numbers_than_current(nums1)}')
print(f'Expected: {expected1}')
print('---')

print(f'Input:    {nums2}')
print(f'Output:   {sol.smaller_numbers_than_current(nums2)}')
print(f'Expected: {expected2}')
print('---')

print(f'Input:    {nums3}')
print(f'Output:   {sol.smaller_numbers_than_current(nums3)}')
print(f'Expected: {expected3}')        