class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        stack = []
        for t in timePoints:
            h,m = map(int,t.split(':'))
            stack.append(60*h + m)
        stack.sort()
        mindiff = float('inf')
        for i in range(1,len(stack)):
            diff = stack[i] - stack[i-1]
            mindiff = min(diff,mindiff)
        return min(mindiff,1440-(stack[-1]-stack[0]))