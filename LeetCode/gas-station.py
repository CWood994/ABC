class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        if sum(gas) < sum(cost) or len(gas) != len(cost):
            return -1
        
        index = 0
        left = 0
        
        for i in range(len(gas)):
            left += (gas[i] - cost[i])
            
            if left < 0:
                index = i + 1
                left = 0
        
        return index
        