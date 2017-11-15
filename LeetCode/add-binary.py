class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # Make both the same length
        length = max(len(a), len(b))
        a = "0" * (length - len(a)) + a
        b = "0" * (length - len(b)) + b

        sum = ""
        carry = 0
        for i in reversed(range(length)):
            col = int(a[i]) + int(b[i]) + carry
            if col == 3:
                sum = "1" + sum
                carry = 1
            elif col == 2:
                sum = "0" + sum
                carry = 1
            elif col == 1:
                sum = "1" + sum
                carry = 0
            else:
                sum = "0" + sum

        if carry != 0:
            sum = str(carry) + sum

        return sum

