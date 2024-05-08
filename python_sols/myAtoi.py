## Accepted solution
class Solution:
    def myAtoi(self, s: str) -> int:
        # Return 0 if string is empty
        if not s:
            return 0
        n = len(s)
        if n == 0:
            return 0
        
        # Removing the starting spaces
        i = 0
        while s[i] == ' ':
            i += 1
            if i == n:
                return 0
            
        # Determining the sign
        sign = -1 if s[i] == '-' else 1
        if s[i] in ['-', '+']:
            i += 1
        res, flag = 0, (2**31 - 1) // 10

        # Converting the string to integer
        while i < n:
            if not s[i].isdigit():
                break
            c = int(s[i])
            if res > flag or (res == flag and c > 7):
                return 2**31 - 1 if sign > 0 else -(2**31)
            res = res * 10 + c
            i += 1
        return sign * res


if __name__ == "__main__":
    obj = Solution()
    obj.myAtoi("012235ab")
