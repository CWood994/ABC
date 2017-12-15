class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        min = self.getMin()
        
        if min ==None or x < min:
            min = x
            
        self.stack.insert(0, (x, min))

    def pop(self):
        """
        :rtype: void
        """
        
        del(self.stack[0])
        

    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[0][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        
        if len(self.stack) == 0:
            return None
        
        return self.stack[0][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()