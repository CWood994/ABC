class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = max_sum = nums[0]

        for i in nums[1:]:
            cur_sum = max(i, cur_sum + i)
            max_sum = max(max_sum, cur_sum)

        return max_sum