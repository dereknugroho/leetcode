class Solution:
    def running_sum(self, nums):
        running_sum = []
        running_num = 0

        for num in nums:
            running_num += num
            running_sum.append(running_num)
        
        return running_sum

# Test cases

sol = Solution()

nums1 = [1, 2, 3, 4]
expected1 = [1, 3, 6, 10]

nums2 = [1, 1, 1, 1, 1]
expected2 = [1, 2, 3, 4, 5]

nums3 = [3, 1, 2, 10, 1]
expected3 = [3, 4, 6, 16, 17]

print(f'Input:    {nums1}')
print(f'Output:   {sol.running_sum(nums1)}')
print(f'Expected: {expected1}')
print('---')

print(f'Input:    {nums2}')
print(f'Output:   {sol.running_sum(nums2)}')
print(f'Expected: {expected2}')
print('---')

print(f'Input:    {nums3}')
print(f'Output:   {sol.running_sum(nums3)}')
print(f'Expected: {expected3}')
