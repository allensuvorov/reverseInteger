import math

class Solution:
    def reverse(self, int):
        rev = 0
        while int!= 0:
            rev *=10
            # push for negativ int
            if int < 0:
                rev += abs(int) % 10 * -1
            # push for positive int
            if int > 0:
                rev += int % 10 # push
            
            # print (int)
            int = math.trunc(float(int)/10) # pop
        return rev

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))