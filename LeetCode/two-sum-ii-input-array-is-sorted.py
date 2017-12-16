class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        low = 0
        high = len(numbers) - 1
        
        while (numbers[low] + numbers[high] != target):
            if numbers[low] + numbers[high] < target:
                low += 1
            else:
                high -= 1
                
        return low+1, high+1