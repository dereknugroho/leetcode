class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1, index2 = None, None

        for i, num1 in enumerate(nums):
            index1 = i
            for j, num2 in enumerate(nums):
                if i != j and num1 + num2 == target:
                    index2 = j
                    return [i, j]
