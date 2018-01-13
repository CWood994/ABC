class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        found = False
        for i in reversed(range(len(nums)-1)):
            if nums[i] < nums[i+1]:
                found = True
                break
                
        if found:
            el = nums[i]
            min_larger = nums[i+1]
            index = i+1
            for j in range(index+1,len(nums)):
                if nums[j] > el and nums[j] < min_larger:
                    index = j
                    min_larger = nums[j]
                    
            nums[i], nums[index] = nums[index], nums[i]
            index=i+1
        else:
            index = 0
         
        b=nums[index:]
        b.sort()
        nums[index:]=b
    
        
        
            
        
        