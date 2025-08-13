class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Edge case: both arrays are empty
        if len(nums1) == 0 and len(nums2) == 0:
            return None

        target_array = []

        # Update target array according to length of input arrays
        if len(nums1) != 0 and len(nums2) != 0:
            target_array = nums1 + nums2
            target_array.sort()
        elif len(nums1) == 0 and len(nums2) != 0:
            target_array = nums2
        elif len(nums1) != 0 and len(nums2) == 0:
            target_array = nums1

        # Calculate median
        if len(target_array) % 2 == 1:
            return float(target_array[int((len(target_array) - 1) / 2)])
        elif len(target_array) % 2 == 0:
            lower_index = int(len(target_array) / 2 - 1)
            upper_index = int(len(target_array) / 2)
            return (target_array[lower_index] + target_array[upper_index]) / 2
