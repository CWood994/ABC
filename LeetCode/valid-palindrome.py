import re

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s is None or s == "":
            return True
        
        new_s = re.sub(r'[^a-zA-Z0-9]', ' ', s)
        new_s = re.sub(r'\s', '', new_s)
        new_s = new_s.lower()
        
        is_pal = True
        for i in range(len(new_s) - 1 //2):
            if new_s[i] != new_s[len(new_s)-1-i]:
                is_pal = False
                break
        
        return is_pal
            
        