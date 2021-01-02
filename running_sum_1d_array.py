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
nums2 = [1, 1, 1, 1, 1]
nums3 = [3, 1, 2, 10, 1]

print('Input:    [1, 2, 3, 4]')
print('Output:  ', sol.running_sum(nums1))
print('Expected: [1, 3, 6, 10]')
print('---')

print('Input:    [1, 1, 1, 1, 1]')
print('Output:  ', sol.running_sum(nums2))
print('Expected: [1, 2, 3, 4, 5]')
print('---')

print('Input:    [3, 1, 2, 10, 1]')
print('Output:  ', sol.running_sum(nums3))
print('Expected: [3, 4, 6, 16, 17]')
