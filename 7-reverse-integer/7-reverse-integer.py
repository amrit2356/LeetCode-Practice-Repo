class Solution:
    def reverse(self, x: int) -> int:
        output = int(''.join([i for i in str(x)][::-1])) if x > 0 else int('-'+''.join([i for i in str(abs(x))][::-1]))
        if((((-2)**31) <= output) and (output <= (2**31 - 1))):
            return output
        else:
            return 0