class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = mini = res = nums[0]

        for num in nums[1:]:
            currMax = max(maxi * num, mini * num, num)
            currMin = min(maxi * num, mini * num, num)
            maxi = currMax
            mini = currMin
            res = max(res, maxi)
        
        return res