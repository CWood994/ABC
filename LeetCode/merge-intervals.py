# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        
        # Sort intervals based on start
        intervals.sort(key=lambda x: x.start)
                
        # Merge if overlapping end/start
        res = []
        start = intervals[0].start
        end = intervals[0].end
        for n in intervals[1:]:
            if n.start > end:
                res.append(Interval(start, end))
                start = n.start
                end = n.end
            else:
                end = max(n.end, end)
        res.append(Interval(start, end))
        return res
            
            
        