class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums_sorted = sorted(nums)
        sol = []

        for i in range(len(nums_sorted)):
            if i == 0 or nums_sorted[i-1] != nums_sorted[i]:
                low = i + 1
                high = len(nums_sorted) - 1
                target = -nums_sorted[i]
                while low < high:
                    if nums_sorted[low] + nums_sorted[high] == target:
                        sol.append([nums_sorted[i], nums_sorted[low], nums_sorted[high]])
                        while low < high and nums_sorted[low] == nums_sorted[low+1]:
                            low += 1
                        while low < high and nums_sorted[high] == nums_sorted[high-1]:
                            high -= 1
                        low += 1
                        high -=1
                        
                    elif nums_sorted[low] + nums_sorted[high] < target:
                        low += 1
                    else:
                        high -= 1

        return sol
                