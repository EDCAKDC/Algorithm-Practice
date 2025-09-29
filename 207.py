from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        learned = 0
        while q:
            v = q.popleft()
            learned += 1
            for j in g[v]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return learned == numCourses
