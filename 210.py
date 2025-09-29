from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        g = defaultdict(list)
        indeg = [0] * numCourses
        res = []
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        while q:
            u = q.popleft()
            res.append(u)
            for v in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return res if len(res) == numCourses else []
