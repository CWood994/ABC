class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = len(s)

        count = 0
        while index > 0 and not s[index - 1].isalpha():
            index -= 1

        while index > 0 and s[index - 1].isalpha():
            count += 1
            index -= 1

        return count


