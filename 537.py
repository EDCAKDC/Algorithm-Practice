class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = num1[:-1].split('+')
        c, d = num2[:-1].split('+')
        a, b, c, d = int(a), int(b), int(c), int(d)
        real = a * c - b * d
        imag = a * d + b * c

        return f'{real}+{imag}i'
