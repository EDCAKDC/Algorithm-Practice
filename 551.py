class Solution:
    def checkRecord(self, s: str) -> bool:
        nA = 0
        nL = 0
        for i in s:
            if i == 'A':
                nA += 1
                if nA >= 2:
                    return False
                nL = 0
            elif i == 'L':
                nL += 1
                if nL >= 3:
                    return False
            else:
                nL = 0
        return True
