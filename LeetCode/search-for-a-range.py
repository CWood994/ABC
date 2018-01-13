class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        
        lo, hi = 0, len(nums) - 1
        mid = (hi+lo)//2
        
        while lo < hi and nums[mid] != target:
            print("mid", lo, hi, mid)
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
                
            mid = (hi+lo)//2
                
        if nums[mid] != target:
            return [-1,-1]
        print(mid)
        lower = mid
        higher = mid
        while lower > 0 and nums[lower-1] == target:
            lower -= 1
        while higher < len(nums)-1 and nums[higher+1] == target:
            higher += 1
            
        return [lower, higher]
        
        
        
        