class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        table = []
        base = ""
        for i in reversed(num1):
            carry = 0
            row = base
            for j in reversed(num2):
                res = int(i) * int(j)
                res += carry
                carry = res // 10
                row = str(res%10) + row
            base = base + "0"
            row = str(carry) + row
            table.append(row)
          
        print(table)
        max_ind = len(max(table, key=len)) - 1
        cur_ind = 0
        count = [0] * (max_ind + 1)
        while cur_ind <= max_ind:
            for s in table:
                if cur_ind > max_ind:
                    break 
                if len(s)-1 < cur_ind:
                    continue
                count[max_ind-cur_ind] += int(s[len(s)-1-cur_ind])
            cur_ind += 1
        print(count) 
        carry = 0
        ans = ""
        for i in reversed(range(len(count))):
            temp = (count[i] + carry)%10
            ans = str(temp) + ans
            carry = (count[i] + carry)//10
          
        for i in range(len(ans)-1):
            if ans[0] == "0":
                ans = ans[1:]
            else:
                break
        return ans