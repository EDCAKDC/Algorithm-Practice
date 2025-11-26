class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev = [w[::-1] for w in words]
        return ' '.join(rev)
