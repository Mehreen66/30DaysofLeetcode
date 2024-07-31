class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        curr = nums[0]
    
        for i in range(1, len(nums)):
          curr = max(curr + nums[i], nums[i])
          ans = max(ans, curr)
    
        return ans