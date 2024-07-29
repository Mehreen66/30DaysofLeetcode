class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [1] * length
    
        product = 1
        for i in range(length):
           result[i] = product
           product =product*nums[i]

        product = 1
        for i in range(length - 1, -1, -1):
          result[i]=result[i]* product
          product=product*nums[i]
    
        return result