class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        store = dict()
        
        for num in range(len(nums)):
            if nums[num] in store:
                return [store[nums[num]], num]
            else:
                store[target - nums[num]] = num
        