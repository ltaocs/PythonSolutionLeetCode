class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if (i-1>=0 and nums[i-1]>nums[i]):
                    nums[i]=nums[i-1]

