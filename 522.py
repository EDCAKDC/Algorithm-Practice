class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(a,b):
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
            return i == len(a)
        strs.sort(key = len, reverse = True)
        for i, s in enumerate(strs):
            if all(
                not is_subseq(s, strs[j])
                for j in range(len(strs))
                if i != j
            ):
                return len(s)
        return -1

from collections import Counter
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(a,b):
            i,j = 0,0
            while i<len(a) and j<len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)
        strs.sort(key = len, reverse = True)
        frequence = Counter(strs)
        for i, s in enumerate(strs):
            if frequence[s] > 1:
                continue
            if all(not is_subseq(s,strs[j]) for j in range(len(strs)) if j!=i ):
                return len(s)
        return -1
            

            