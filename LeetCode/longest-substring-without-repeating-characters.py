class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        store = ""
        max_count = 0
        for c in s:
            if c in store:
                max_count = max(len(store), max_count)
                store = store.split(c)[1]
                store += c
            else:
                store += c
                
        return max(len(store), max_count)
        