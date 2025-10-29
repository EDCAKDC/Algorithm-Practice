class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        a = sum(machines)
        if a%n != 0:
            return -1
        avg = a//n
        res = 0
        flow = 0
        for x in machines:
            load = x -avg
            flow += load
            res = max(res,max(abs(flow),load))
        return res
