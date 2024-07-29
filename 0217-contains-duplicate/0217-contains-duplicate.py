class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            l += 1
            r += 1
        return False
        