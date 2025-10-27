class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        def mul(a, b):
            return (
                a[0]*b[0]+a[1]*b[2], a[0]*b[1] + a[1]*b[3],
                a[2]*b[0]+a[3]*b[2], a[2]*b[1] + a[3]*b[3],
            )

        def mat_pow(p):
            res = ((1, 0, 0, 1))
            base = (1, 1, 1, 0)
            while p:
                if p & 1:
                    res = mul(res, base)
                base = mul(base, base)
                p >>= 1
            return res
        qn = mat_pow(n)
        return qn[2]
