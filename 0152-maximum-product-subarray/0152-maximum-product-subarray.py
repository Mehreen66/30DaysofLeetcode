class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = minimum = ans = nums[0]

        for num in nums[1:]:
            currMax = max(maximum * num, minimum * num, num)
            currMin = min(maximum * num, minimum * num, num)
            maximum = currMax
            minimum = currMin
            ans = max(ans, maximum)
        
        return ans