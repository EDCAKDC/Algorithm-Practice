class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def sub_seq(s, w):
            i = j = 0
            while i < len(s) and j < len(w):
                if s[i] == w[j]:
                    j += 1
                i += 1
            return j == len(w)
        dictionary.sort(key=lambda w: (-len(w), w))
        for w in dictionary:
            if sub_seq(s, w):
                return w
        return ''
