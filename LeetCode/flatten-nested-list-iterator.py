class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nums=[]
        self.pos=0
        self.process(nestedList)
        
        
    def next(self):
        """
        :rtype: int
        """
        res = self.nums[self.pos]
        self.pos += 1
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pos < len(self.nums)
    
    def process(self, nums):
        if type(nums) == NestedInteger and nums.isInteger():
            self.nums.append(nums)
        else:
            if type(nums) == NestedInteger:
                for x in nums.getList():
                    self.process(x)
            else:
                 for x in nums:
                    self.process(x)