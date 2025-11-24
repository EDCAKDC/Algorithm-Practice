class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = {}
        for raw in wall:
            pos = 0
            for brick in raw[:-1]:
                pos += brick
                edge_count[pos] = edge_count.get(pos,0) + 1
        if not edge_count:
            return len(wall)
        return len(wall) - max(edge_count.values())   
        