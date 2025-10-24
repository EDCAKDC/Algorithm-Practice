class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            sign = '-'
        elif num == 0:
            return '0'
        else:
            sign=''
        num = abs(num)
        res = []
        while num:
            res.append(str(num%7))
            num //= 7
        return sign+''.join(reversed(res))