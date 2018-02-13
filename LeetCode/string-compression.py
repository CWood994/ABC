class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        if not chars:
            return 0
        
        # End of current cur array
        new = 0
        count = 1
        prev = chars[0]
          
        for i in range(1,len(chars)):
            if chars[i] == prev:
                count += 1
            else:
                chars[new] = prev
                new += 1
                if count > 1:
                    tmp = [s for s in str(count)]
                    chars[new:new+len(tmp)] = tmp
                    new += len(tmp)
                prev = chars[i]
                count = 1
            
        chars[new] = prev
        if count > 1:
            new += 1
            chars[new:] = [s for s in str(count)]
        else:
            chars[new+1:] = []
            
        return len(chars)
            
        