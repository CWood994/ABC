class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
    
        start = 0
        stop = 0
        for i in range(len(s)):
            print(str(i)+": \n")
            len1 = self.expandCenter(s, i, i)
            len2 = self.expandCenter(s, i, i+1)
            len3 = max(len1, len2)
            if len3 > stop-start:
                start = i - (len3-1)/2
                stop = i + len3/2
                print("start:" + str(start) + " , stop:" + str(stop))
            
        return s[start+1:stop]
            
            
    def expandCenter(self, s, start, stop):
        
        while start >= 0 and stop < len(s) and s[start] == s[stop]:
            start -= 1
            stop += 1
            
            
        return stop-start+1
        