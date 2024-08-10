class Solution:
    def running_sum(self, nums):
        running_sum = []
        running_num = 0

        for num in nums:
            running_num += num
            running_sum.append(running_num)
        
        return running_sum
