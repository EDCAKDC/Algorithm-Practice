class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        k = len(digits)
        i = k - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i < 0:
            return -1
        j = k - 1
        while digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        left, right = i + 1, k - 1
        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1
        ans = int(''.join(digits))
        return ans if ans <= 2**31 - 1 else -1