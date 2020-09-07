import math

class Solution:
    def reverse(self, int):
        int_max = pow(2,31)-1
        int_min = pow(-2,31)
        rev = 0
        while int!= 0:
            # get the last digit
            pop = abs(int) % 10
            if int < 0:
                pop *= -1

            # check if rev is about to overflow
            if rev > (int_max/10) or (rev == int_max/10 and pop > 7):
                return 0
            if rev < (int_min/10) or (rev == int_min/10 and pop < -8):
                return 0

            # push
            rev = rev*10 + pop 

            # pop
            int = math.trunc(float(int)/10)
        return rev

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))

# print(pow(2,31)-1) #  2147483647
# print(pow(-2,31))  # -2147483648